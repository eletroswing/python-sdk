"""
    Module: pix-qr-code
"""
from openpix.http import HttpClient
import openpix.resources.pix_qr_code_types as pix_qr_code_types
from openpix.types import PagePayload

class PixQrCode():
    """
    Access to PixQrCode  

    [Click here for more info](https://developers.woovi.com/api#tag/pixQrCode)  # pylint: disable=line-too-long
    """
    def __init__(self, HttpClient: HttpClient):
        self._client = HttpClient

    """Get one Pix QrCode.
    Args:
        id (str): pixQrCode ID, correlation ID or emv identifier.
    
        [Click here for more info](https://developers.openpix.com.br/api#tag/pixQrCode/paths/~1api~1v1~1qrcode-static~1%7Bid%7D/get)
    """
    def get(self, id: str) -> pix_qr_code_types.PixQrCodeList:
        return self._client.get(path=f'/api/v1/qrcode-static/{id}')

    """Get a list of Pix QrCodes.
    Args:
        page (PageInfo): A class for page info object containing limit and skip
    
        [Click here for more info](https://developers.openpix.com.br/api#tag/pixQrCode/paths/~1api~1v1~1qrcode-static/get)
    """
    def list(self, page: PagePayload = PagePayload()) -> pix_qr_code_types.PixQrCodeList:
        return self._client.get(path=f'/api/v1/partner/qrcode-static', query={"limit": page.limit, "skip": page.skip})

    """Create a new Pix QrCode Static
    Args:
        name (str): Name of this pix qrcode
        correlationID (str): Your correlation ID to keep track of this qrcode
        value (int): Value in cents of this qrcode
        comment (str): Comment to be added in infoPagador
    
        [Click here for more info](https://developers.openpix.com.br/api#tag/pixQrCode/paths/~1api~1v1~1qrcode-static/post)
    """
    def create(self, name: str, correlationID: str, value: int, comment: str) -> pix_qr_code_types.PixQrCodeCreate:
        return self._client.post(path=f'/api/v1/partner/qrcode-static', data={
          "name": name,
          "correlationID": correlationID,
          "value": value,
          "comment": comment
        })