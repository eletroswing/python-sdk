from openpix.types import PageInfo
from typing import List

class TaxIDObjectPayload:
    def __init__(self, taxID: str, type: str):
        self.taxID = taxID
        self.type = type

class PreRegistrationUserObject:
    def __init__(self, firstName: str, lastName: str, email: str, phone: str):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phone = phone

class CompanyObjectPayload:
    def __init__(self, id: str, name: str, taxID: TaxIDObjectPayload):
        self.id = id
        self.name = name
        self.taxID = taxID

class AccountObjectPayload:
    def __init__(self, clientId: str):
        self.clientId = clientId

class PreRegistrationObjectPayload:
    def __init__(self, name: str, taxID: TaxIDObjectPayload, user: PreRegistrationUserObject, 
                 company: CompanyObjectPayload, account: AccountObjectPayload):
        self.name = name
        self.taxID = taxID
        self.user = user
        self.company = company
        self.account = account

class Application:
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type


class TaxId:
    def __init__(self, taxID: str, type: str):
        self.taxID = taxID
        self.type = type

class PreRegistrationCreate:
    def __init__(self, name: str, website: str, taxID: TaxId):
        self.name = name
        self.taxID = taxID
        self.website = website

class PreRegistration:
    def __init__(self, preRegistration: PreRegistrationObjectPayload, user: PreRegistrationUserObject, company: CompanyObjectPayload, account: AccountObjectPayload):
        self.preRegistration = preRegistration
        self.user = user
        self.company = company
        account = account

class PartnerGet:
    def __init__(self, preRegistration: PreRegistration):
        self.preRegistration = preRegistration

class PartnerList: 
    def __init__(self, pageInfo: PageInfo, preRegistrations: List[PreRegistration]):
        self.pageInfo = pageInfo
        self.preRegistrations = preRegistrations
