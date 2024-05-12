"""
    Module: charge
"""
from openpix.http import HttpClient
import charge_types
from typing import List, Union, Optional

class Charge:
    """
    Access to Charge  

    [Click here for more info](https://developers.woovi.com/api#tag/charge)  # pylint: disable=line-too-long
    """
    def __init__(self, HttpClient: HttpClient):
        self._client = HttpClient

    """Get a charge
    Args:
        id (str): charge ID or correlation ID.
        [Click here for more info](https://developers.woovi.com/api#tag/charge/paths/~1api~1v1~1charge~1%7Bid%7D/delete)
    """
    def get(self, id: str) -> charge_types.ChargeGet:
        return self._client.get(path=f'/api/v1/charge/{id}')

    """Get a list of charges.
    Args:
        start (str): Start date used in the query. Complies with RFC 3339.. 
        end (str): End date used in the query. Complies with RFC 3339. 
        status (str): Enum: "ACTIVE" "COMPLETED" "EXPIRED"
        customer (str): Customer Correlation ID
        limit (int): number of content per page
        skip (int): number of how many contents will be ignored
        [Click here for more info](https://developers.woovi.com/api#tag/charge/paths/~1api~1v1~1charge/get)
    """
    def list(self, start: str = None, end: str = None, status: str = None, customer: str = None, limit: int = 10, skip: int = 0) -> charge_types.ChargeList:
        return self._client.get(path=f'/api/v1/charge/', query={"limit": limit, "skip": skip, start: start, end: end, status: status, customer: customer})

    """Delete one charge request
    Args:
        id (str): charge ID or correlation ID.
        [Click here for more info](https://developers.woovi.com/api#tag/charge/paths/~1api~1v1~1charge~1%7Bid%7D/delete)
    """
    def delete(self, id:str) -> charge_types.ChargeDelete:
        return self._client.delete(path=f'/api/v1/charge/{id}')

    """create a charge
    Args:
        return_existing (bool, optional): Make the endpoint idempotent, will return an existent charge if already has a one with the correlationID.

        correlationID (str): Your correlation ID to keep track of this charge.
        value (int): Value in cents of this charge.
        type (str, optional): Charge type. Enum: "DYNAMIC" "OVERDUE". Determines whether a charge will have a deadline, fines, and interests.
        comment (str, optional): Comment to be added in infoPagador.
        identifier (str, optional): Custom identifier for EMV.
        expiresIn (int, optional): Expires the charge in seconds (minimum is 15 minutes).
        expiresDate (str, optional): Expiration date of the charge. Only in ISO 8601 format.
        customer (CustomerPayload, optional): Customer information.
        daysForDueDate (int, optional): Time in days until the charge hits the deadline so fines and interests start applying. Only considered for charges of type OVERDUE.
        daysAfterDueDate (int, optional): Time in days that a charge is still payable after the deadline. Only considered for charges of type OVERDUE.
        interests (Interests, optional): Interests configuration. Only considered for charges of type OVERDUE.
        fines (Fines, optional): Fines configuration. Only considered for charges of type OVERDUE.
        discountSettings (dict, optional): Discount settings for the charge. Only considered for charges of type OVERDUE.
        additionalInfo (List[AdditionalInfoItem], optional): Additional info of the charge.
        enableCashbackPercentage (bool, optional): True to enable cashback and false to disable.
        enableCashbackExclusivePercentage (bool, optional): True to enable fidelity cashback and false to disable.
        [Click here for more info](https://developers.woovi.com/api#tag/charge/paths/~1api~1v1~1charge/post)
    """
    def create(self, return_existing: bool = True, correlationID: str = "", value: int = 0, type: Optional[str] = None, comment: Optional[str] = None,
                 identifier: Optional[str] = None, expiresIn: Optional[int] = None, expiresDate: Optional[str] = None,
                 customer: Optional[charge_types.CustomerPayload] = None, daysForDueDate: Optional[int] = None,
                 daysAfterDueDate: Optional[int] = None, interests: Optional[charge_types.Interests] = None,
                 fines: Optional[charge_types.Fines] = None, discountSettings: Optional[dict] = None,
                 additionalInfo: Optional[List[charge_types.AdditionalInfoItem]] = None, enableCashbackPercentage: Optional[bool] = None,
                 enableCashbackExclusivePercentage: Optional[bool] = None) -> charge_types.ChargeCreate:
       return self._client.post(path=f'/api/v1/charge/', query={"return_existing": return_existing}, data={
           correlationID: correlationID,
           value: value,
           type: type,
           comment: comment,
           identifier: identifier,
           expiresIn: expiresIn,
           expiresDate: expiresDate,
           customer: customer,
           daysAfterDueDate: daysAfterDueDate,
           daysForDueDate: daysForDueDate,
           fines: fines,
           interests: interests,
           discountSettings: discountSettings,
           additionalInfo: additionalInfo,
           enableCashbackExclusivePercentage: enableCashbackExclusivePercentage,
           enableCashbackPercentage: enableCashbackPercentage
       })


    """Get the qr code from a charge
    Args:
        id (str): charge link payment ID.
        size (int): Size for the image. This size should be between 600 and 4096. if the size parameter was not passed, the default value will be 1024.
        [Click here for more info](https://developers.woovi.com/api#tag/charge/paths/~1openpix~1charge~1brcode~1image~1%7B:id%7D.png?size=1024/get)
    """
    def getQrImage(self, id: str, size: int = 1024) -> str:
        return f'https://api.woovi.com/openpix/charge/brcode/image/{id}.png?size={size}'