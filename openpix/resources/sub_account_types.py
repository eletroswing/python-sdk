from openpix.types import PageInfo
from typing import List

class SubAccount:
    def __init__(self, name: str, pixKey: str, balance: int):
        self.name = name
        self.pixKey = pixKey
        self.balance = balance

class Transaction:
    def __init__(self, status: str, value: int, correlationID: str, destinationAlias: str, comment: str):
        self.status = status
        self.value = value
        self.correlationID = correlationID
        self.destinationAlias = destinationAlias
        self.comment = comment

class SubAccountCreate:
    def __init__(self, name: str, pixKey: str):
        self.name = name
        self.pixKey = pixKey

class DestinationSubaccount:
    def __init__(self, name: str, pixKey: str, value: int):
        self.name = name
        self.pixKey = pixKey
        self.value = value

class OriginSubaccount:
    def __init__(self, name: str, pixKey: str, value: int):
        self.name = name
        self.pixKey = pixKey
        self.value = value

class SubAccountGet:
    def __init__(self, SubAccount: SubAccount):
        self.SubAccount = SubAccount

class SubAccountList: 
    def __init__(self, pageInfo: PageInfo, subAccounts: List[SubAccount]):
        self.pageInfo = pageInfo
        self.subAccounts = subAccounts

class WithdrawCreate:
    def __init__(self, transaction: Transaction):
        self.transaction = transaction

class SubAccountCreate:
    def __init__(self, SubAccount: SubAccountCreate):
        self.SubAccount = SubAccount

class TransferCreate:
    def __init__(self, value: int, destinationSubaccount: DestinationSubaccount, originSubaccount: OriginSubaccount):
        self.value = value
        self.destinationSubaccount = destinationSubaccount
        self.originSubaccount = originSubaccount
