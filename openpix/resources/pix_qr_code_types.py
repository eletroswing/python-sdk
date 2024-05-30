from openpix.types import PageInfo
from typing import List

class PixQrCode:
    def __init__(self, name: str, value: str, comment: str, brCode: str, correlationID: str, 
                 paymentLinkID: str, paymentLinkUrl: str, qrCodeImage: str, createdAt: str, updatedAt: str):
        self.name = name
        self.value = value
        self.comment = comment
        self.brCode = brCode
        self.correlationID = correlationID
        self.paymentLinkID = paymentLinkID
        self.paymentLinkUrl = paymentLinkUrl
        self.qrCodeImage = qrCodeImage
        self.createdAt = createdAt
        self.updatedAt = updatedAt


class PixQrCodeGet:
    def __init__(self, pixQrCode: PixQrCode):
        self.pixQrCode = pixQrCode

class PixQrCodeList: 
    def __init__(self, pageInfo: PageInfo, pixQrCodes: List[PixQrCode]):
        self.pageInfo = pageInfo
        self.pixQrCodes = pixQrCodes
    
class PixQrCodeCreate: 
    def __init__(self, pixQrCode: PixQrCode):
        self.pixQrCode = pixQrCode
