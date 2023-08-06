import typing
import logging
import json

import requests


class Utils:

    @staticmethod
    def to_json_str(obj: typing.Any) -> str:
        return json.dumps(obj, indent=4)

    @staticmethod
    def try_load_json(json_str: str) -> typing.Tuple[typing.Any, str]:
        try:
            return json.loads(json_str), None
        except Exception as e:
            return None, e

    @staticmethod
    def log_and_raise(msg: str, logger: logging.Logger = None) -> None:
        if logger:
            logger.exception(msg)
        else:
            print(f"ERROR: {msg}")
        raise Exception(msg)

    @staticmethod
    def request_check_status(response: requests.Response) -> None:
        if response.status_code != 200:
            response.raise_for_status()

    @staticmethod
    def is_empty(x: typing.Any) -> bool:
        return x is None or len(x) == 0

    @staticmethod
    def non_empty(x: typing.Any) -> bool:
        return not Utils.is_empty(x)

    @staticmethod
    def clean_model_name(model_name: str) -> str:
        # TODO: make clean stronger
        if model_name is None or len(model_name) == "":
            return "empty_model"
        for c in [" ", ".", "/", "\\", "*"]:
            model_name = model_name.replace(c, "_")
        return model_name
