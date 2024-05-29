from openpix.types import PageInfo
from typing import List

class PaymentDestination:
    def __init__(self, name: str, taxID: str, pixKey: str, bank: str, branch: str, account: str):
        self.name = name
        self.taxID = taxID
        self.pixKey = pixKey
        self.bank = bank
        self.branch = branch
        self.account = account

class PaymentTransaction:
    def __init__(self, value: int, endToEndId: str, time: str):
        self.value = value
        self.endToEndId = endToEndId
        self.time = time

class Payment:
    def __init__(self, value: int, destinationAlias: str, destinationAliasType: str, qrCode: str, correlationID: str, 
                 comment: str, status: str, sourceAccountId: str, transaction: PaymentTransaction, destination: PaymentDestination):
        self.value = value
        self.destinationAlias = destinationAlias
        self.destinationAliasType = destinationAliasType
        self.qrCode = qrCode
        self.correlationID = correlationID
        self.comment = comment
        self.status = status
        self.sourceAccountId = sourceAccountId
        self.transaction = transaction
        self.destination = destination

class PaymentGet:
    def __init__(self, payment: Payment, transaction: PaymentTransaction, destination: PaymentDestination):
        self.payment = payment
        self.transaction = transaction
        self.destination = destination

class PaymentList: 
    def __init__(self, pageInfo: PageInfo, payments: List[PaymentGet]):
        self.pageInfo = pageInfo
        self.payments = payments

class PaymentApprove:
    def __init__(self, payment: Payment, transaction: PaymentTransaction, destination: PaymentDestination):
        self.payment = payment
        self.transaction = transaction
        self.destination = destination

class PaymentCreate:
    def __init__(self, payment: Payment):
        self.payment = payment