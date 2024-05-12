class Transfer:
    def __init__(self, value: int, time: str, correlationID: str):
        self.value = value
        self.time = time
        self.correlationID = correlationID

class TransferCreate:
    def __init__(self, transaction: Transfer):
        self.transaction = transaction
    