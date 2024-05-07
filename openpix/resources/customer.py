"""
    Module: customer
"""
from openpix.http import HttpClient

class Customer:
    """
    Access to Customer  

    [Click here for more info](https://developers.woovi.com/api#tag/customer)  # pylint: disable=line-too-long
    """
    def __init__(self, HttpClient: HttpClient):
        self._client = HttpClient

    def get(self):
        return

    def list(self):
        return

    def create(self):
        return