"""
    Module: transfer
"""
from openpix.http import HttpClient
import openpix.resources.transfer_types as transfer_types

class Transfer:
    """
    Access to Transfer  

    [Click here for more info](https://developers.woovi.com/api#tag/transfer-(request-access))  # pylint: disable=line-too-long
    """
    def __init__(self, HttpClient: HttpClient):
        self._client = HttpClient

    def create(self, value: str, fromPixKey: str, toPixKey: str) -> transfer_types.Transfer:
        return self._client.post(path=f'/api/v1/transfer', data={value: value, fromPixKey: fromPixKey, toPixKey: toPixKey})