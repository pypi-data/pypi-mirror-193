from .api_client import ApiClient
from .configuration import Configuration
from .api.reservations_api import (
    ReservationsApi,
)


class ResviewApi:
    def __init__(self, user_token=None, server_url=None, **kwargs):
        all_kwargs = {
            "host": server_url,
            "discard_unknown_keys": True,
            **kwargs,
        }
        if user_token is not None:
            all_kwargs = {
                "api_key": {"tokenAuth": user_token},
                "api_key_prefix": {"tokenAuth": "Token"},
                **all_kwargs,
            }
        config = Configuration(**all_kwargs)
        self.client = ApiClient(config)
        self._reservations_api = ReservationsApi(self.client)

    @property
    def reservations_api(self) -> ReservationsApi:
        return self._reservations_api
