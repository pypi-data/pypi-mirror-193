import typing

import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text

class TestBertModel:

    TF_MODEL_FEATURES = {
        "input_text": tf.io.FixedLenFeature(shape=(), dtype=tf.string)
    }
    TF_OUTPUT_LENGTH = 128

    def create_tf_bert_model(self) -> tf.keras.Model:
        # See more examples in: https://tfhub.dev/tensorflow/bert_en_uncased_L-12_H-768_A-12/4
        preprocessor_url = "https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3"
        encoder_url = "https://tfhub.dev/tensorflow/small_bert/bert_en_uncased_L-2_H-128_A-2/2"


        # Bert layers
        bert_preprocessor_layer = hub.KerasLayer(preprocessor_url)
        bert_encoder_layer = hub.KerasLayer(encoder_url, trainable=True)

        input_text_layer = tf.keras.layers.Input(shape=(), dtype=tf.string, name="input_text")
        X = bert_preprocessor_layer(input_text_layer)
        bert_outputs = bert_encoder_layer(X)

        pooled_output = bert_outputs["pooled_output"]      # [batch_size, bert_vec_length].
        #sequence_output = bert_outputs["sequence_output"]  # [batch_size, seq_length, bert_vec_length].

        model = tf.keras.Model(inputs=[input_text_layer], outputs={"sentence_embedding": pooled_output})
        model.summary()
        return model

    def export_model(self, model: tf.keras.Model, export_path: str):
        print(f"Exporting TF2 model to path={export_path}")
        tf.keras.models.save_model(
            model,
            export_path,
            overwrite=True,
            include_optimizer=True,
            save_format=None,
            signatures=self.create_model_signature_tf2(model, TestBertModel.TF_MODEL_FEATURES),
            options=None
        )

    def create_model_signature_tf2(self, model: tf.keras.Model, features_spec: typing.Dict[str, typing.Any]):
        #TF 2: https://stackoverflow.com/questions/58769933/serving-a-tensorflow-2-keras-model-with-feature-columns-and-preprocessing-migra
        @tf.function(input_signature=[tf.TensorSpec(shape=[None], dtype=tf.string, name=TensorFlowServingWrapper.INPUT_NAME)])
        def parse_examples_proto(serialized_examples):
            # Parse string serialization of Examples
            parsed_examples = tf.io.parse_example(serialized_examples, features_spec)
            # Invoke model with parsed examples
            return model(parsed_examples)

        return parse_examples_proto

    def test_bert_encode_text(self, text_items: typing.List[str], model: tf.keras.Model) -> typing.Dict[str, typing.Any]:
        sentences = tf.constant(text_items)
        return model(sentences)