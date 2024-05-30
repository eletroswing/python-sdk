"""
    Module: refund
"""
from openpix.http import HttpClient
openpix.resources.
from openpix.types import PagePayload

class Refund:
    """
    Access to Refund  

    [Click here for more info](https://developers.woovi.com/api#tag/refund)  # pylint: disable=line-too-long
    """
    def __init__(self, HttpClient: HttpClient):
        self._client = HttpClient

    """get a refund
    Args:
        id (str): identifier of your refund.

        [Click here for more info](https://developers.openpix.com.br/api#tag/refund/paths/~1api~1v1~1refund~1%7Bid%7D/get)
    """
    def get(self, id: str) -> refund_types.RefundGet:
        return self._client.get(path=f'/api/v1/refund/{id}')

    """list refunds
    Args:
        page (PageInfo): A class for page info object containing limit and skip
    
        [Click here for more info](https://developers.openpix.com.br/api#tag/refund/paths/~1api~1v1~1refund/get)
    """
    def list(self, page: PagePayload = PagePayload()) -> refund_types.RefundList:
        return self._client.get(path=f'/api/v1/refund', query={"limit": page.limit, "skip": page.skip})

    """create a refund
    Args:
        value (int): value of the refund.   
        transactionEndToEndId (str): Your transaction ID, or endToEnd ID, to keep track of this refund
        correlationID (str): Your correlation ID, unique identifier refund
        comment (str): Comment of this refund. Maximum length of 140 characters.
    
        [Click here for more info](https://developers.openpix.com.br/api#tag/refund/paths/~1api~1v1~1refund/post)
    """
    def create(self, value: int, transactionEndToEndId: str, correlationID: str, comment: str) -> refund_types.RefundCreate:
        return self._client.post(path=f'/api/v1/refund', data={
            'comment': comment,
            'correlationID': correlationID,
            'transactionEndToEndId': transactionEndToEndId,
            'value': value
        })