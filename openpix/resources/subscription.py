"""
    Module: subscription
"""
from openpix.http import HttpClient

class Subscription:
    """
    Access to Subscription  

    [Click here for more info](https://developers.woovi.com/api#tag/subscription)  # pylint: disable=line-too-long
    """
    def __init__(self, HttpClient: HttpClient):
        self._client = HttpClient

    def get(self):
        return

    def create(self):
        return