"""
    Module: charge_refund
"""
from openpix.http import HttpClient
openpix.resources.
from openpix.types import PagePayload

class ChargeRefund:
    """
    Access to ChargeRefund  

    [Click here for more info](https://developers.woovi.com/api#tag/charge-refund)  # pylint: disable=line-too-long
    """
    def __init__(self, HttpClient: HttpClient):
        self._client = HttpClient

    """Get a list of charge refunds.
    Args:
        id (str): The correlation ID of the charge. 
        limit (int): number of content per page
        skip (int): number of how many contents will be ignored
        [Click here for more info](https://developers.woovi.com/api#tag/charge-refund/paths/~1api~1v1~1charge~1%7Bid%7D~1refund/get)
    """
    def list(self, id: str, page: PagePayload = PagePayload()) -> charge_refund_types.ChargeRefundList:
        return self._client.get(path=f'/api/v1/charge/{id}/refund', query={"limit": page.limit, "skip": page.skip})

    """Create a new refund for a charge
    Args:
        id (str): The correlation ID of the charge. 
        correlationID (str): Your correlation ID to keep track for this refund
        value (int): Value in cents for this refund
        comment (str): Comment for this refund. Maximum length of 140 characters.
        [Click here for more info](https://developers.woovi.com/api#tag/charge-refund/paths/~1api~1v1~1charge~1%7Bid%7D~1refund/post)
    """
    def create(self, id: str, correlationID: str, value: int, comment: str) -> charge_refund_types.ChargeRefundCreate:
        return self._client.post(path=f'/api/v1/charge/{id}/refund', data={value: value, correlationID: correlationID, comment: comment})