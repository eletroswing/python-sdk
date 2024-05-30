"""
    Module: transactions
"""
from openpix.http import HttpClient
import transactions_type

class Transactions:
    """
    Access to Transactions  

    [Click here for more info](https://developers.woovi.com/api#tag/transactions)  # pylint: disable=line-too-long
    """
    def __init__(self, HttpClient: HttpClient):
        self._client = HttpClient

    """Get a Transaction
    Args:
        id (str): you can use the transaction id from openpix or the endToEndId of transaction from bank

        [Click here for more info](https://developers.openpix.com.br/api#tag/transactions/paths/~1api~1v1~1transaction~1%7Bid%7D/get)
    """
    def get(self, id: str) -> transactions_type.TransactionsGet:
        return self._client.get(path=f'/api/v1/transaction/{id}')

    """Get a list of transactions
    Args:
        start (str): Start date used in the query. Complies with RFC 3339.
        end	(str): End date used in the query. Complies with RFC 3339.
        charge (str): You can use the charge ID or correlation ID or transaction ID of charge to get a list of transactions related of this transaction
        pixQrCode (str): You can use the QrCode static ID or correlation ID or identifier field of QrCode static to get a list of QrCode related of this transaction
        withdrawal (str): You can use the ID or EndToEndId of a withdrawal transaction to get all transactions related to the withdrawal

        limit (int, optional): itens per page, defaults 10.
        skip (int, optional): how many itens are gonna be skipped, default 0.
        
        [Click here for more info](https://developers.openpix.com.br/api#tag/transactions/paths/~1api~1v1~1transaction/get)
    """ 
    def list(self, start: str, end: str, charge: str, pixQrCode: str, withdrawal: str, limit: int = 10, skip: int = 0) -> transactions_type.TransactionsList:
        return self._client.get(path=f'/api/v1/transaction', query={"start": start, "end": end, "charge": charge, "pixQrCode": pixQrCode, "withdrawal": withdrawal, "limit": limit, "skip": skip})
