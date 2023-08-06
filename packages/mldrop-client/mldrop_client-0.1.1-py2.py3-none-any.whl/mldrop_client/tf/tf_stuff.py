def deploy_tf2_keras_model(self, model_metadata: ModelMetadata, tf_keras_model: typing.Any,
                           tf_model_features: typing.Dict[str, typing.Any]) -> ModelMetadata:
    import tensorflow as tf

    def create_model_signature_tf2(model: tf.keras.Model, features_spec: typing.Dict[str, typing.Any]):
        # TF 2: https://stackoverflow.com/questions/58769933/serving-a-tensorflow-2-keras-model-with-feature-columns-and-preprocessing-migra
        @tf.function(
            input_signature=[tf.TensorSpec(shape=[None], dtype=tf.string, name=MLDropClient.TF_EXAMPLES_INPUT_NAME)])
        def parse_examples_proto(serialized_examples):
            # Parse string serialization of Examples
            parsed_examples = tf.io.parse_example(serialized_examples, features_spec)
            # Invoke model with parsed examples
            return model(parsed_examples)

        return parse_examples_proto

    def export_model(model: tf.keras.Model, export_path: str):
        tf.keras.models.save_model(
            model,
            export_path,
            overwrite=True,
            include_optimizer=True,
            save_format=None,
            signatures=create_model_signature_tf2(model, tf_model_features),
            options=None
        )

    with tempfile.TemporaryDirectory() as tmp_dir_path:
        # Export TF model to tmp dir
        self.logger.info(f"Exporting TF2 Keras model to tmp path={tmp_dir_path}")
        export_model(tf_keras_model, tmp_dir_path)

        # Do deploy
        return self.deploy_model(model_metadata, tmp_dir_path)