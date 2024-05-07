"""
Module: sdk
"""
from openpix.http import HttpClient
from openpix.resources import (
    Account,
    CashbackFidelity,
    Charge,
    ChargeRefund,
    Customer,
    Partner,
    PixQrCode,
    Payment,
    Refund,
    SubAccount,
    Subscription,
    Transactions,
    Transfer,
    Webhook
)

class SDK:
    """Generate access to all API' modules, which are:

        1. Account
        2. CashbackFidelity
        3. Charge
        4. ChargeRefund
        5. Customer
        6. Partner
        7: PixQrCode
        8: Payment
        9: Refund
        10: SubAccount
        11: Subscription
        12: Transactions
        13: Transfer
        14: Webhook
    """

    def __init__(
        self,
        app_id: str,
    ):
        """Construct ur SDK Object to have access to all APIs modules.
        Args:
            app_id (str): A string representing the application ID, which serves as the API key.
            [Click here for more info](https://developers.woovi.com/docs/apis/api-getting-started)
        """
        self._http_client = HttpClient(app_id=app_id)

    @property
    def account(self):
        """
        Returns the attribute value of the function
        """
        return Account(self._http_client)

    @property
    def cashback(self):
        """
        Returns the attribute value of the function
        """
        return CashbackFidelity(self._http_client)
    
    @property
    def charge(self):
        """
        Returns the attribute value of the function
        """
        return Charge(self._http_client)
    
    @property
    def chargeRefund(self):
        """
        Returns the attribute value of the function
        """
        return ChargeRefund(self._http_client)

    @property
    def customer(self):
        """
        Returns the attribute value of the function
        """
        return Customer(self._http_client)
    
    @property
    def partner(self):
        """
        Returns the attribute value of the function
        """
        return Partner(self._http_client)
    
    @property
    def pixQrCode(self):
        """
        Returns the attribute value of the function
        """
        return PixQrCode(self._http_client)
    
    @property
    def payment(self):
        """
        Returns the attribute value of the function
        """
        return Payment(self._http_client)
    
    @property
    def refund(self):
        """
        Returns the attribute value of the function
        """
        return Refund(self._http_client)

    @property
    def subAccount(self):
        """
        Returns the attribute value of the function
        """
        return SubAccount(self._http_client)

    @property
    def subscription(self):
        """
        Returns the attribute value of the function
        """
        return Subscription(self._http_client)
    
    @property
    def transactions(self):
        """
        Returns the attribute value of the function
        """
        return Transactions(self._http_client)
    
    @property
    def transfer(self):
        """
        Returns the attribute value of the function
        """
        return Transfer(self._http_client)
    
    @property
    def webhook(self):
        """
        Returns the attribute value of the function
        """
        return Webhook(self._http_client)