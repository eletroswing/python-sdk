"""
    Module: refund
"""
from openpix.http import HttpClient

class Refund:
    """
    Access to Refund  

    [Click here for more info](https://developers.woovi.com/api#tag/refund)  # pylint: disable=line-too-long
    """
    def __init__(self, HttpClient: HttpClient):
        self._client = HttpClient

    def get(self):
        return

    def list(self):
        return

    def getQrImage(self):
        return