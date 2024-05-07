"""
    Module: partner
"""
from openpix.http import HttpClient

class Partner:
    """
    Access to Partner  

    [Click here for more info](https://developers.woovi.com/api#tag/partner-(request-access))  # pylint: disable=line-too-long
    """
    def __init__(self, HttpClient: HttpClient):
        self._client = HttpClient

    def get(self):
        return

    def list(self):
        return

    def delete(self):
        return

    def createPreRegistration(self):
        return

    def createApplication(self):
        return