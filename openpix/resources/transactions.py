"""
    Module: transactions
"""
from openpix.http import HttpClient

class Transactions:
    """
    Access to Transactions  

    [Click here for more info](https://developers.woovi.com/api#tag/transactions)  # pylint: disable=line-too-long
    """
    def __init__(self, HttpClient: HttpClient):
        self._client = HttpClient
        
    def get(self):
        return

    def list(self):
        return