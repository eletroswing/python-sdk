"""
    Module: sub-account
"""
from openpix.http import HttpClient
import sub_account_types
from openpix.types import PagePayload

class SubAccount():
    """
    Access to SubAccount  

    [Click here for more info](https://developers.woovi.com/api#tag/sub-account-(request-access))  # pylint: disable=line-too-long
    """
    def __init__(self, HttpClient: HttpClient):
        self._client = HttpClient

    """Get subaccount details
    Args:
        id (str): pix key registered to the subaccount
        
        [Click here for more info](https://developers.openpix.com.br/api#tag/sub-account-(request-access)/paths/~1api~1v1~1subaccount~1%7Bid%7D/get)
    """ 
    def get(self, id: str) -> sub_account_types.SubAccountGet:
        return self._client.get(path=f'/api/v1/subaccount/{id}')
    
    """Get a list of subaccounts
    Args:
        page (PageInfo): A class for page info object containing limit and skip
        
        [Click here for more info](https://developers.openpix.com.br/api#tag/sub-account-(request-access)/paths/~1api~1v1~1subaccount/get)
    """ 
    def list(self, page: PagePayload = PagePayload()) -> sub_account_types.SubAccountList:
        return self._client.get(path=f'/api/v1/subaccount', query={"limit": page.limit, "skip": page.skip})

    """Create a subaccount
    Args:
        id (str): pix key registered to the subaccount
        
        [Click here for more info](https://developers.openpix.com.br/api#tag/sub-account-(request-access)/paths/~1api~1v1~1subaccount~1%7Bid%7D~1withdraw/post)
    """ 
    def withdraw(self, id: str) -> sub_account_types.WithdrawCreate:
        return self._client.post(path=f'/api/v1/subaccount/{id}/withdraw')

    """Create a subaccount
    Args:
        pixKey (str): The pix key for the sub account
        name (str): Name of the sub account
        
        [Click here for more info](https://developers.openpix.com.br/api#tag/sub-account-(request-access)/paths/~1api~1v1~1subaccount/post)
    """ 
    def create(self, pixKey: str, name: str) -> sub_account_types.SubAccountCreate:
        return self._client.post(path=f'/api/v1/subaccount', data={
          "pixKey": pixKey,
          "name": name
        })
    
    """Transfer between subaccounts
    Args:
        value (int): The value of the transfer in cents
        fromPixKey (str): The transfer origin pix key
        fromPixKeyType (str): The transfer origin pix key type. Enum: "CPF" "CNPJ" "EMAIL" "PHONE" "RANDOM"
        toPixKey (str): The transfer destination pix key
        toPixKeyType (str): The transfer destination pix key type. Enum: "CPF" "CNPJ" "EMAIL" "PHONE" "RANDOM"
        correlationID (str): Your correlation ID to keep track of this transfer
        
        [Click here for more info](https://developers.openpix.com.br/api#tag/sub-account-(request-access)/paths/~1api~1v1~1subaccount~1transfer/post)
    """ 
    def transfer(self, value: int, fromPixKey: str, fromPixKeyType: str, toPixKey: str, toPixKeyType: str, correlationID: str) -> sub_account_types.TransferCreate:
        return self._client.post(path=f'/api/v1/subaccount/transfer', data={
          "value": value,
          "fromPixKey": fromPixKey,
          "fromPixKeyType": fromPixKeyType,
          "toPixKey": toPixKey,
          "toPixKeyType": toPixKeyType,
          "correlationID": correlationID,
        })