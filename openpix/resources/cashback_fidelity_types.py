class CashbackInfo:
    def __init__(self, value: int):
        self.value: value

class CashbackGet:
    def __init__(self, balance: int, status: str):
        self.balance = balance
        self.status = status

class CashbackCreate:
    def __init__(self, cashback: CashbackInfo, message: str):
        self.cashback = cashback
        self.message = message