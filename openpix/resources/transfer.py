"""
    Module: transfer
"""
class Transfer:
    """
    Access to Transfer  

    [Click here for more info](https://developers.woovi.com/api#tag/transfer-(request-access))  # pylint: disable=line-too-long
    """
    def __init__(self, HttpClient):
        self._client = HttpClient

    def create(self):
        return