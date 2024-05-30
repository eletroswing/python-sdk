from openpix.types import PageInfo
from typing import List

class Webhook:
    def __init__(self, id: str, name: str, event: str, url: str, authorization: str, isActive: bool, createdAt: str, updatedAt: str):
        self.id = id
        self.name = name
        self.event = event
        self.url = url
        self.authorization = authorization
        self.isActive = isActive
        self.createdAt = createdAt
        self.updatedAt = updatedAt

class WebhookListIps:
    def __init__(self, ips: List[str]):
        self.ips = ips

class WebhookList:
    def __init__(self, pageInfo: PageInfo, webhooks: List[Webhook]):
        self.pageInfo = pageInfo
        self.webhooks = webhooks

class WebhookDelete: 
    def __init__(self, status: str):
        self.status = status

class WebhookCreate: 
    def __init__(self, webhook: Webhook):
        self.webhook = webhook
