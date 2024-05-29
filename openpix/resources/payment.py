"""
    Module: payment
"""
from openpix.http import HttpClient
import payment_types

class Payment:
    """
    Access to Payment  

    [Click here for more info](https://developers.woovi.com/api#tag/payment-(request-access))  # pylint: disable=line-too-long
    """
    def __init__(self, HttpClient: HttpClient):
        self._client = HttpClient

    """get a payment
    Args:
        id (str): identifier of your payment.

        [Click here for more info](https://developers.openpix.com.br/api#tag/payment-(request-access)/paths/~1api~1v1~1payment~1%7Bid%7D/get)
    """
    def get(self, id: str) -> payment_types.PaymentGet:
        return self._client.get(path=f'/api/v1/payment/{id}')

    """list payments
    Args:
        limit (int, optional): itens per page, defaults 10.
        skip (int, optional): how many itens are gonna be skipped, default 0.
    
        [Click here for more info](https://developers.openpix.com.br/api#tag/payment-(request-access)/paths/~1api~1v1~1payment~1%7Bid%7D/get)
    """
    def list(self, limit: int = 10, skip: int = 0) -> payment_types.PaymentList:
        return self._client.get(path=f'/api/v1/payment', query={"limit": limit, "skip": skip})

    """approve a payment
    Args:
        correlationID (str): the correlation ID of the payment to be approved

        [Click here for more info](https://developers.openpix.com.br/api#tag/payment-(request-access)/paths/~1api~1v1~1payment~1approve/post)
    """
    def approve(self, correlationID: str) -> payment_types.PaymentApprove:
        return self._client.post(path=f'/api/v1/payment/approve', data={
            "correlationID": correlationID
        })
    
    """create a payment
    Args:
        To a pix key: 
            value (int): value of the requested payment in cents
            destinationAlias (str): the pix key the payment should be sent to
            destinationAliasType (str): the type of the pix key the payment should be sent to
            correlationID (str): an unique identifier for your payment
            comment (str): the comment that will be send alongisde your payment
            sourceAccountId	(str): an optional id for the source account of the payment, if not informed will assume the default account
        
        To a qr code: 
            qrCode (int): the QR Code to be paid
            correlationID (str): an unique identifier for your payment
            comment (str): the comment that will be send alongisde your payment
            sourceAccountId	(str): an optional id for the source account of the payment, if not informed will assume the default account

        [Click here for more info](https://developers.openpix.com.br/api#tag/payment-(request-access)/paths/~1api~1v1~1payment/post)
    """
    def create(self, **kwargs) -> payment_types.PaymentCreate: 
        return self._client.post(path=f'/api/v1/payment', data=kwargs)