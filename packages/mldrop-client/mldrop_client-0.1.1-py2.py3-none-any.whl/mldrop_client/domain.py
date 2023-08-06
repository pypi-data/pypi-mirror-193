import typing


class ModelMetadata:
    def __init__(self, model_name: str, inputs: typing.List['ModelInputDef'], outputs: typing.List['ModelOutputDef'],
                 description: str, major_version: int, minor_version: int,
                 sample_invocation: typing.List[typing.Dict[str, typing.Any]]):
        self.model_id = ""
        self.short_publish_code = ""
        self.model_name = model_name
        self.description = description
        self.major_version = major_version
        self.minor_version = minor_version
        self.model_type = ModelType.TENSOR_FLOW
        self.inputs = inputs
        self.outputs = outputs
        self.sample_invocation = sample_invocation

        # TODO: run validations


class ModelType:
    TENSOR_FLOW: str = "TENSOR_FLOW"


class InputType:
    TYPE_STRING: str = "STRING"
    TYPE_FLOAT: str = "FLOAT"
    TYPE_INT: str = "INTEGER"
    TYPE_STRING_LIST: str = "STRING_LIST"
    TYPE_FLOAT_LIST: str = "FLOAT_LIST"
    TYPE_INT_LIST: str = "INTEGER_LIST"
    TYPE_FLOAT_LIST_VARLEN: str = "FLOAT_LIST_VARLEN"
    TYPE_INT_LIST_VARLEN: str = "INT_LIST_VARLEN"
    TYPE_STRING_LIST_VARLEN: str = "STRING_LIST_VARLEN"
    TYPE_IMAGE_URL: str = "IMAGE_URL"


class ModelInputDef:
    def __init__(self, name: str, input_type: str = InputType.TYPE_STRING, default_value: str = "", shape: typing.List[int] = None):
        self.name = name
        self.input_type = input_type
        self.default_value = default_value
        self.shape = shape


class ModelOutputDef:
    def __init__(self, name: str, output_type: str = InputType.TYPE_FLOAT, shape: typing.List[int] = None):
        self.name = name
        self.output_type = output_type
        self.shape = shape


class ModelInvocationRequest:
    def __init__(self, request_id: str):
        self.request_id = request_id
        self.samples: typing.List[typing.Dict[str, typing.Any]] = []