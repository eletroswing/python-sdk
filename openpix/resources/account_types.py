from openpix.types import PageInfo
from typing import List

class BalanceInfo:
    def __init__(self, total: int, blocked: int, available: int):
        self.total = total
        self.blocked = blocked
        self.available = available

class AccountInfo:
    def __init__(self, accountId: str, isDefault: bool, balance: BalanceInfo):
        self.accountId = accountId
        self.balance = balance
        self.isDefault = isDefault

class TransactionInfo:
    def __init__(self, endToEndId: str, value: int):
        self.endToEndId = endToEndId
        self.value = value

class WithdrawInfo:
    def __init__(self, account: AccountInfo, transaction: TransactionInfo):
        self.account = account
        self.transaction = transaction

class AccountGet:
    def __init__(self, account: AccountInfo):
        self.account = account


class AccountList: 
    def __init__(self, pageInfo: PageInfo, accounts: List[AccountInfo]):
        self.pageInfo = pageInfo
        self.accounts = accounts

class AccountWithdraw:
    def __init__(self, withdraw: WithdrawInfo):
        self.withdraw = withdraw