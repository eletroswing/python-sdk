"""
    Module: cashback_fidelity
"""
from openpix.http import HttpClient
import openpix.resources.cashback_fidelity_types as cashback_fidelity_types

class CashbackFidelity:
    """
    Access to CashbackFidelity  

    [Click here for more info](https://developers.woovi.com/api#tag/cashback-fidelity)  # pylint: disable=line-too-long
    """
    def __init__(self, HttpClient: HttpClient):
        self._client = HttpClient
    
    """Get one fidelity.
    Args:
        taxID (str): the user's tax id document
        [Click here for m   ore info](https://developers.woovi.com/api#tag/cashback-fidelity/paths/~1api~1v1~1cashback-fidelity~1balance~1%7BtaxID%7D/get)
    """
    def get(self, taxID: str) -> cashback_fidelity_types.CashbackGet:
        return self._client.get(path=f'/api/v1/cashback-fidelity/balance/{taxID}')

    """Create one fidelity.
    Args:
        taxID (str): the user's tax id document
        value (int): the fidelity value
        [Click here for more info](https://developers.woovi.com/api#tag/cashback-fidelity/paths/~1api~1v1~1cashback-fidelity/post)
    """
    def create(self, taxID: str, value: int) -> cashback_fidelity_types.CashbackCreate:
        return self._client.post(path=f'/api/v1/cashback-fidelity', data={value: value, taxID: taxID})