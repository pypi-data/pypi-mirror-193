from mldrop_client.client import MLDropClient


def init(access_token: str, host: str = MLDropClient.DEFAULT_SERVER_HOST) -> MLDropClient:
    """
    Init MLDrop client
    :param access_token: the access token you received when creating a new account.
    :param host:
    :return: MLDropClient
    """
    return MLDropClient(access_token, host=host)

