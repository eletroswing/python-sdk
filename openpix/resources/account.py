"""
    Module: account
"""
from openpix.http import HttpClient
import account_types

class Account:
    """
    Access to Accounts

    [Click here for more info](https://developers.woovi.com/api#tag/account)  # pylint: disable=line-too-long
    """
    def __init__(self, HttpClient: HttpClient):
        self._client = HttpClient

    """Get one account.
    Args:
        accountId (str): the account unique identifier
        [Click here for more info](https://developers.woovi.com/api#tag/account)
    """
    def get(self, accountId: str) -> account_types.AccountInfo:
        return self._client.get(path=f'/api/v1/account/{accountId}')

    """Get a list of accounts.
    Args:
        limit (int): number of content per page
        skip (int): number of how many contents will be ignored
        [Click here for more info](https://developers.woovi.com/api#tag/account/paths/~1api~1v1~1account~1/get)
    """
    def list(self, limit: int = 10, skip: int = 0) -> account_types.AccountList:
        return self._client.get(path=f'/api/v1/account', query={"limit": limit, "skip": skip})

    """Make a withdraw.
    Args:
        accountId (str): the account unique identifier
        value (int): the value for the withdraw
        [Click here for more info](https://developers.woovi.com/api#tag/account/paths/~1api~1v1~1account~1%7BaccountId%7D~1withdraw/post)
    """
    def withdraw(self, accountId: str, value: int) -> account_types.AccountWithdraw:
        return self._client.post(path=f'/api/v1/account/{accountId}', data={value: value})