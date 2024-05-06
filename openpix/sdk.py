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
        app_id,
    ):
        """Construct ur SDK Object to have access to all APIs modules.
        Args:
            [Click here for more info](https://developers.woovi.com/docs/apis/api-getting-started)
        """
        self._http_client = HttpClient(app_id=app_id)

    @property
    def account(self):
        """
        Returns the attribute value of the function
        """
        return Account(HttpClient)

    @property
    def cashback_fidelity(self):
        """
        Returns the attribute value of the function
        """
        return CashbackFidelity(HttpClient)
    
    @property
    def charge(self):
        """
        Returns the attribute value of the function
        """
        return Charge(HttpClient)
    
    @property
    def charge_refund(self):
        """
        Returns the attribute value of the function
        """
        return ChargeRefund(HttpClient)

    @property
    def customer(self):
        """
        Returns the attribute value of the function
        """
        return Customer(HttpClient)
    
    @property
    def partner(self):
        """
        Returns the attribute value of the function
        """
        return Partner(HttpClient)
    
    @property
    def pix_qr_code(self):
        """
        Returns the attribute value of the function
        """
        return PixQrCode(HttpClient)
    
    @property
    def payment(self):
        """
        Returns the attribute value of the function
        """
        return Payment(HttpClient)
    
    @property
    def refund(self):
        """
        Returns the attribute value of the function
        """
        return Refund(HttpClient)

    @property
    def sub_account(self):
        """
        Returns the attribute value of the function
        """
        return SubAccount(HttpClient)

    @property
    def subscription(self):
        """
        Returns the attribute value of the function
        """
        return Subscription(HttpClient)
    
    @property
    def transactions(self):
        """
        Returns the attribute value of the function
        """
        return Transactions(HttpClient)
    
    @property
    def transfer(self):
        """
        Returns the attribute value of the function
        """
        return Transfer(HttpClient)
    
    @property
    def webhook(self):
        """
        Returns the attribute value of the function
        """
        return Webhook(HttpClient)