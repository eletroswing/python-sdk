from openpix.types import PageInfo
from typing import List

class Refund:
    def __init__(self, value: int, status: str, correlationID: str, refundId: str, time: str, comment: str):
        self.value = value
        self.status = status
        self.correlationID = correlationID	
        self.refundId = refundId
        self.time = time
        self.comment = comment

class RefundGet:
    def __init__(self, pixTransactionRefund: Refund):
        self.pixTransactionRefund = pixTransactionRefund

class RefundCreate:
    def __init__(self, refund: Refund):
        self.refund = refund

class RefundList: 
    def __init__(self, pageInfo: PageInfo, refunds: List[Refund]):
        self.pageInfo = pageInfo
        self.refunds = refunds
