import typing
import logging
from pathlib import Path
import os

import numpy as np
import torch

from mldrop_client.domain import ModelMetadata, ModelOutputDef, ModelInputDef, InputType
from mldrop_client.common.http_client import HttpClient, Utils


class MLDropClient:

    TF_EXAMPLES_INPUT_NAME: str = "serialized_examples"
    DEFAULT_SERVER_HOST: str = "https://api.scattering.ai"

    def __init__(self, access_token: str, host: str = DEFAULT_SERVER_HOST, base_url: str = "/api/v1/",
                 upload_temp_folder: str = "__model_tmp"):
        self.logger = logging.getLogger(__name__)
        self.access_token = access_token
        self.http_client = HttpClient(host, base_url)
        self.upload_temp_folder = upload_temp_folder

        # Validate token
        is_valid = bool(self.http_client.do_get(f"token/validate?t={access_token}", "validate_token", "", output_key = "valid"))
        if is_valid:
            account_url = host + f"/?t={access_token}"
            print(f"MLDrop client is READY to use, browse account details in URL: {account_url}")
        else:
            if access_token == "USE_YOUR_ACCOUNT_TOKEN":
                raise Exception(f"You are using the DEMO account token [USE_YOUR_ACCOUNT_TOKEN]. You can create a new account in: https://www.scattering.ai/signup")
            raise Exception(f"Invalid account token [{access_token}]. You can create a new account in: https://www.scattering.ai/signup")



    def create_model_metadata(self, model_name: str, inputs: typing.List[ModelInputDef],
                              outputs: typing.List[ModelOutputDef], description: str = "", major_version: int = 1,
                              minor_version: int = 0,
                              sample_invocation: typing.List[typing.Dict[str, typing.Any]] = []) -> ModelMetadata:
        print(f"Created model metadata for model: {model_name}, inputs: {len(inputs)}, outputs: {len(outputs)}, invocation samples: {len(sample_invocation)}")
        return ModelMetadata(model_name, inputs, outputs, description, major_version, minor_version, sample_invocation)

    def input_type(self, name: str, input_type: str, default_value: str, shape: typing.List[int] = None) -> ModelInputDef:
        return ModelInputDef(name, input_type, default_value, shape)

    def input_string(self, name: str, default_value: str = "") -> ModelInputDef:
        return self.input_type(name, input_type=InputType.TYPE_STRING, default_value=default_value)

    def input_image_url(self, name: str, default_value: str = "") -> ModelInputDef:
        return self.input_type(name, input_type=InputType.TYPE_IMAGE_URL, default_value=default_value)

    def input_float(self, name: str, default_value: float = 0) -> ModelInputDef:
        return self.input_type(name, input_type=InputType.TYPE_FLOAT, default_value=str(default_value))

    def input_int(self, name: str, default_value: int = 0) -> ModelInputDef:
        return self.input_type(name, input_type=InputType.TYPE_INT, default_value=str(default_value))

    def input_float_list(self, name: str, default_value: float = [], shape: typing.List[int] = None,
                         variable_length: bool = False) -> ModelInputDef:
        # TODO: convert default_value as json dump
        input_type = InputType.TYPE_FLOAT_LIST_VARLEN if variable_length else InputType.TYPE_FLOAT_LIST
        return self.input_type(name, input_type=input_type, default_value=str(default_value), shape=shape)

    def input_int_list(self, name: str, default_value: float = [], shape: typing.List[int] = None,
                         variable_length: bool = False) -> ModelInputDef:
        # TODO: convert default_value as json dump
        input_type = InputType.TYPE_INT_LIST_VARLEN if variable_length else InputType.TYPE_INT_LIST
        return self.input_type(name, input_type=input_type, default_value=str(default_value), shape=shape)

    def input_string_list(self, name: str, default_value: float = [], shape: typing.List[int] = None,
                          variable_length: bool = False) -> ModelInputDef:
        # TODO: convert default_value as json dump
        input_type = InputType.TYPE_STRING_LIST_VARLEN if variable_length else InputType.TYPE_STRING_LIST
        return self.input_type(name, input_type=input_type, default_value=str(default_value), shape=shape)

    # TODO: add all others InputType

    def output_type(self, name: str, output_type: str, shape: typing.List[int] = None) -> ModelOutputDef:
        return ModelOutputDef(name, output_type, shape)

    def output_float(self, name: str) -> ModelOutputDef:
        return self.output_type(name, output_type=InputType.TYPE_FLOAT)

    def output_int(self, name: str) -> ModelOutputDef:
        return self.output_type(name, output_type=InputType.TYPE_INT)

    def output_string(self, name: str) -> ModelOutputDef:
        return self.output_type(name, output_type=InputType.TYPE_STRING)

    def output_string_list(self, name: str) -> ModelOutputDef:
        return self.output_type(name, output_type=InputType.TYPE_STRING_LIST)

    def output_float_list(self, name: str, shape: typing.List[int] = None) -> ModelOutputDef:
        return self.output_type(name, output_type=InputType.TYPE_FLOAT_LIST, shape=shape)

    # TODO: add all others output types

    def _deploy_model_from_file(self, model_metadata: ModelMetadata, local_model_path: str) -> str:
        pass
        try:
            self.logger.info(f"Deploying model with metadata={model_metadata}, model_path={local_model_path}")

            # TODO: check file exist and looks fine
            # Upload file to server and obtain blob_id
            params = {
                "t": self.access_token,
                "model_name": model_metadata.model_name
            }
            file_size_mb = round(os.path.getsize(local_model_path) / 1024.0 / 1024.0, 2)
            print(f"Uploading model [{model_metadata.model_name}] with size={file_size_mb} MB.")
            with open(local_model_path, "rb") as file:
                files = {"file": file}
                upload_resp = self.http_client.do_file_upload("modelstore", files, params)
            blob_id = upload_resp["blob_id"]
            self.logger.info(f"Model blob_id={blob_id}")

            # Upload model metadata
            metadata_param = {
                "access_token": self.access_token,
                "blob_id": blob_id,
                "version_major": model_metadata.major_version,
                "version_minor": model_metadata.minor_version,
                "model_type": model_metadata.model_type,
                "model_name": model_metadata.model_name, # TODO: add support for model_name in server
                "description": model_metadata.description,
                "model_inputs": [{"name": i.name, "input_type": i.input_type, "default_value": i.default_value, "shape": i.shape} for i in model_metadata.inputs],
                "model_outputs": [{"name": i.name, "output_type": i.output_type, "shape": i.shape} for i in model_metadata.outputs],
                "sample_invocation": model_metadata.sample_invocation,
            }
            metadata_resp = self.http_client.do_put_post("POST", "model", metadata_param)
            # TODO: validate response
            model_id = metadata_resp["model_id"]
            self.logger.info(f"model_id={model_id}")
            short_publish_code = ""

            # Update model metadata
            model_metadata.model_id = model_id
            model_metadata.short_publish_code = short_publish_code
            return short_publish_code

        except Exception as e:
            Utils.log_and_raise(f"Error deploying model={model_metadata} with model_path={local_model_path}, error={e}")

    def deploy_pytorch_model(self, model_metadata: ModelMetadata, pytorch_model: torch.nn.Module) -> str:
        """
        Deploy Pytorch model.
        Model is first exported to TorchScript using scripting.
        :param model_metadata: metadata of the model
        :param pytorch_model: the Pytorch module
        :return: model ID, use it to invoke the model
        """
        try:
            self.logger.info(f"Exporting PyTorch model={model_metadata.model_name} to TorchScript")
            pytorch_model.eval()
            scripted_model = torch.jit.script(pytorch_model)
        except Exception as e:
            Utils.log_and_raise(f"Error exporting PyTorch module to TorchScript, error={e}")
            return ""

        return self.deploy_torchscript_model(model_metadata, scripted_model)

    def deploy_torchscript_model(self, model_metadata: ModelMetadata, scripted_model: torch.ScriptModule) -> str:
        """
        Deploy the given TorchScript model
        :param model_metadata: metadata of the model
        :param scripted_model: the TorchScript module
        :return: model ID, use it to invoke the model
        """
        # Save torch model to a tmp file
        tmp_path = self._save_model_to_tmp_file(model_metadata, scripted_model)

        # Do deploy
        short_publish_code = self._deploy_model_from_file(model_metadata, tmp_path)
        os.remove(tmp_path)

        print(f"Model [{model_metadata.model_name}] SUCCESSFULLY deployed. Invoke using model_id={model_metadata.model_id}")
        model_url = self.http_client.host + f"/model/{model_metadata.model_id}?t={self.access_token}"
        print(f"Browse model details in URL: {model_url}")
        return model_metadata.model_id

    def invoke_model(self, model_id: str, samples: typing.List[typing.Dict[str, typing.Any]],
                     request_id: str = "") -> typing.List[typing.Dict[str, typing.Any]]:
        """
        Invoke model with a lists of samples, pointing to the previously deployed model_id
        :param model_id: ID of the model you want to invoke
        :param samples: list of samples to invoke the model, each sample as key-value dictionary for all required features
        :param request_id:
        :return: output of the model, one entry for each input sample in the same order
        """
        # TODO: validate inputs and that metadata contains short_publish_code

        url = f"model/invoke"
        params = {
            "request_id": request_id, # TODO: add request_id in server
            "t": self.access_token,
            "model_id": model_id,
            "samples": self._process_samples(samples),
        }
        return self.http_client.do_put_post("POST", url, params)

    def delete_model(self, model_id) -> bool:
        url = f"/api/v1/model/delete?t={self.access_token}&model_id={model_id}"
        self.http_client.do_get(url, "delete_model", "")
        return True

    def _process_samples(self, samples: typing.List[typing.Dict[str, typing.Any]]) \
            -> typing.List[typing.Dict[str, typing.Any]]:
        out_samples = []
        for sample in samples:
            out_sample = {}
            out_samples.append(out_sample)
            for key in sample.keys():
                value = sample[key]

                # Convert torch Tensor as a flat list of values
                if type(value) == torch.Tensor:
                    tensor: torch.Tensor = value
                    out_sample[key] = tensor.tolist()

                elif type(value) == np.ndarray:
                    arr: np.ndarray = value
                    out_sample[key] = arr.tolist()

                else:
                    out_sample[key] = value

        return out_samples

    def _save_model_to_tmp_file(self, model_metadata: ModelMetadata, scripted_model: torch.ScriptModule) -> str:
        # Tmp output path
        Path(self.upload_temp_folder).mkdir(parents=True, exist_ok=True)
        tmp_path = os.path.join(self.upload_temp_folder, f"{Utils.clean_model_name(model_metadata.model_name)}.pt")
        self.logger.info(f"Saving TorchScript model={model_metadata.model_name} to tmp path={tmp_path}")
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

        # Save torch model to a tmp file
        scripted_model.save(tmp_path)
        return tmp_path






