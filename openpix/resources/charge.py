"""
    Module: charge
"""
from openpix.http import HttpClient

class Charge:
    """
    Access to Charge  

    [Click here for more info](https://developers.woovi.com/api#tag/charge)  # pylint: disable=line-too-long
    """
    def __init__(self, HttpClient: HttpClient):
        self._client = HttpClient

    def get(self):
        return

    def list(self):
        return

    def delete(self):
        return

    def create(self):
        return

    def getQrImage(self):
        return