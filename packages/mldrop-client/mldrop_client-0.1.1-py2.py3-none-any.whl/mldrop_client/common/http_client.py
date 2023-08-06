import logging
import typing
import requests
from mldrop_client.common.utils import Utils

class HttpClient:
    BASE_HEADER = {
        "Content-Type": "application/json",
    }

    def __init__(self, host: str, base_url: str):
        self.logger = logging.getLogger(__name__)
        self.host = host
        self.base_url = base_url

    @staticmethod
    def request_check_status(response: requests.Response) -> None:
        if response.status_code != 200:
            response.raise_for_status()

    def do_get(self, endpoint_url: str, name: str, value: str, base_url: str = None,
               output_key: str = "object") -> typing.Any:
        try:
            base_url = self.base_url if base_url is None else base_url
            url = self.host + base_url + endpoint_url
            self.logger.info(f"Getting {name}: {value} from url: {url}")
            r = requests.get(url, headers=HttpClient.BASE_HEADER)
            HttpClient.request_check_status(r)
            resp_json = r.json()
            self.logger.info(f"GET {name} response: {resp_json}")
            if output_key is None:
                return resp_json
            if output_key in resp_json:
                return resp_json[output_key]
            raise Exception(f"Invalid response getting {name}: value from service, response: {resp_json}")
        except Exception as e:
            Utils.log_and_raise(f"Error getting {name}: {value} from service, error: {e}", self.logger)

    def do_put_post(self, method: str, endpoint_url: str, obj: typing.Any, json_body: bool = True,
                    base_url: str = None) -> typing.Union[typing.List, typing.Dict]:
        try:
            base_url = self.base_url if base_url is None else base_url
            url = self.host + base_url + endpoint_url
            body = (Utils.to_json_str(obj) if json_body else obj) if obj else None
            self.logger.info(f"{method} into service endpoint: {url}, body: {body}")
            headers = HttpClient.BASE_HEADER
            if method == "PUT":
                r = requests.put(url, data=body, headers=headers)
            elif method == "POST":
                r = requests.post(url, data=body, headers=headers)
            elif method == "DELETE":
                r = requests.delete(url, data=body, headers=headers)
            else:
                raise Exception(f"Invalid requests method: {method}")
            HttpClient.request_check_status(r)
            resp_json = r.json()
            self.logger.info(f"{method} response: {resp_json}")
            return resp_json
        except Exception as e:
            Utils.log_and_raise(
                f"Error performing {method} into service, object: {obj}, error: {e}", self.logger)

    def do_file_upload(self, endpoint_url: str, files: dict, params: typing.Dict[str, typing.Any]):
        url = self.host + self.base_url + endpoint_url
        try:
            r = requests.post(url, files=files, data=params)
            HttpClient.request_check_status(r)
            resp_json = r.json()
            return resp_json
        except Exception as e:
            Utils.log_and_raise(
                f"Error performing file upload into url={url}, files: {files.keys()}, params: {params}, error: {e}", self.logger)


    @staticmethod
    def to_url_params(params: dict) -> str:
        return "&".join(f"{k}={v}" for k, v in params.items())