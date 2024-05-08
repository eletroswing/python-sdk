from openpix.types import PageInfo
from typing import List

class ChargeRefund:
    def __init__(self, status: str, value: int, correlationID: str, endToEndId: str, time: str):
        self.status = status
        self.value = value
        self.correlationID = correlationID
        self.endToEndId = endToEndId
        self.time = time

class ChargeRefundCreate:
    def __init__(self, status: str, value: int, correlationID: str, endToEndId: str, time: str, comment: str):
        self.status = status
        self.value = value
        self.correlationID = correlationID
        self.endToEndId = endToEndId
        self.time = time
        self.comment = comment

class ChargeRefundList: 
    def __init__(self, pageInfo: PageInfo, refunds: List[ChargeRefund]):
        self.pageInfo = pageInfo
        self.refunds = refunds

class ChargeRefundCreate: 
    def __init__(self, refund: ChargeRefundCreate):
        self.refund = refund