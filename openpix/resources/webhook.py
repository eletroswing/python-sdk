"""
    Module: webhook
"""
from openpix.http import HttpClient
openpix.resources.
from openpix.types import PagePayload

class Webhook:
    """
    Access to Webhook  

    [Click here for more info](https://developers.woovi.com/api#tag/webhook)  # pylint: disable=line-too-long
    """
    def __init__(self, HttpClient: HttpClient):
        self._client = HttpClient

    """Get a list of webhook IPs
    Args:
        page (PageInfo): A class for page info object containing limit and skip
    
        [Click here for more info](https://developers.openpix.com.br/api#tag/webhook/paths/~1api~1v1~1webhook~1ips/get)
    """
    def list_ips(self, page: PagePayload = PagePayload()) -> webhook_types.WebhookListIps:
        return self._client.get(path=f'/api/v1/webhook/ips', query={"limit": page.limit, "skip": page.skip})

    """Get a list of webhooks
    Args:
        page (PageInfo): A class for page info object containing limit and skip
    
        [Click here for more info](https://developers.openpix.com.br/api#tag/webhook/paths/~1api~1v1~1webhook/get)
    """
    def list(self, page: PagePayload = PagePayload()) -> webhook_types.WebhookList:
        return self._client.get(path=f'/api/v1/webhook', query={"limit": page.limit, "skip": page.skip})

    """Delete a Webhook
    Args:
        id (str): A class for page info object containing limit and skip
    
        [Click here for more info](https://developers.openpix.com.br/api#tag/webhook/paths/~1api~1v1~1webhook~1%7Bid%7D/delete)
    """
    def delete(self, id: str) -> webhook_types.WebhookDelete:
        return self._client.delete(path=f'/api/v1/webhook/{id}')

    """Create a new Webhook
    Args:
        id (str): identifier of the webhook
        name (str): the name of the webhook
        event (str): Available events to register a webhook to listen to. If no one selected anyone the default event will be OPENPIX:TRANSACTION_RECEIVED.
        url (str): webhook endpoint to be called
        isActive (bool): if the endpoint is active
        authorization (str): authorization to your endpoint
    
        [Click here for more info](https://developers.openpix.com.br/api#tag/webhook/paths/~1api~1v1~1webhook/post)
    """
    def create(self, name: str, event: str, url: str, authorization: str, isActive: bool) -> webhook_types.WebhookCreate:
        return self._client.post(path=f'/api/v1/webhook', data={
            "webhook": {
                "name": name,
                "event": event,
                "url": url,
                "isActive": isActive,
                "authorization": "authorization"
            }
        })
