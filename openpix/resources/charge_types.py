from openpix.types import PageInfo
from typing import List, Union, Optional

class ChargeDelete:
    def __init__(self, status: str, id: str):
        self.status = status
        self.id = id

class CustomerPayload:
    def __init__(self, name: str, taxID: Optional[str] = None, email: Optional[str] = None, phone: Optional[str] = None):
        self.name = name
        self.taxID = taxID
        self.email = email
        self.phone = phone

class Interests:
    def __init__(self, value: int):
        self.value = value

class Fines:
    def __init__(self, value: int):
        self.value = value

class DiscountFixedDate:
    def __init__(self, daysActive: int, value: int):
        self.daysActive = daysActive
        self.value = value


class DiscountSettings:
    def __init__(self, modality: str, discountFixedDate: DiscountFixedDate):
        self.modality = modality
        self.discountFixedDate = discountFixedDate

class AdditionalInfoItem:
    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value

class ChargeCreate:
    def __init__(self, correlationID: str, value: int, type: Optional[str] = None, comment: Optional[str] = None,
                 identifier: Optional[str] = None, expiresIn: Optional[int] = None, expiresDate: Optional[str] = None,
                 customer: Optional[CustomerPayload] = None, daysForDueDate: Optional[int] = None,
                 daysAfterDueDate: Optional[int] = None, interests: Optional[Interests] = None,
                 fines: Optional[Fines] = None, discountSettings: Optional[DiscountSettings] = None,
                 additionalInfo: Optional[List[AdditionalInfoItem]] = None, enableCashbackPercentage: Optional[bool] = None,
                 enableCashbackExclusivePercentage: Optional[bool] = None):
        self.correlationID = correlationID
        self.value = value
        self.type = type
        self.comment = comment
        self.identifier = identifier
        self.expiresIn = expiresIn
        self.expiresDate = expiresDate
        self.customer = customer
        self.daysForDueDate = daysForDueDate
        self.daysAfterDueDate = daysAfterDueDate
        self.interests = interests
        self.fines = fines
        self.discountSettings = discountSettings
        self.additionalInfo = additionalInfo
        self.enableCashbackPercentage = enableCashbackPercentage
        self.enableCashbackExclusivePercentage = enableCashbackExclusivePercentage
        
class TaxID:
    def __init__(self, taxID: str, type: str):
        self.taxID = taxID
        self.type = type

class Address:
    def __init__(self, zipcode: str, street: str, number: str, neighborhood: str, city: str, state: str, complement: str, country: str):
        self.zipcode = zipcode
        self.street = street
        self.number = number
        self.neighborhood = neighborhood
        self.city = city
        self.state = state
        self.complement = complement
        self.country = country

class Customer:
    def __init__(self, name: str, email: str, phone: str, taxID: TaxID, correlationID: str, address: Address):
        self.name = name
        self.email = email
        self.phone = phone
        self.taxID = taxID
        self.correlationID = correlationID
        self.address = address

class AdditionalInfoItem:
    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value

class Charge:
    def __init__(self, value: int, customer: Customer, comment: str, brCode: str, status: str,
                 correlationID: str, paymentLinkID: str, paymentLinkUrl: str, globalID: str,
                 transactionID: str, identifier: str, qrCodeImage: str, additionalInfo: List[AdditionalInfoItem],
                 pixKey: str, createdAt: str, updatedAt: str, expiresIn: str):
        self.value = value
        self.customer = customer
        self.comment = comment
        self.brCode = brCode
        self.status = status
        self.correlationID = correlationID
        self.paymentLinkID = paymentLinkID
        self.paymentLinkUrl = paymentLinkUrl
        self.globalID = globalID
        self.transactionID = transactionID
        self.identifier = identifier
        self.qrCodeImage = qrCodeImage
        self.additionalInfo = additionalInfo
        self.pixKey = pixKey
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        self.expiresIn = expiresIn

class EasyCharge:
    def __init__(self, value: int, customer: Customer, comment: str, brCode: str, status: str,
                 correlationID: str, paymentLinkID: str, paymentLinkUrl: str, qrCodeImage: str, additionalInfo: List[AdditionalInfoItem], createdAt: str, updatedAt: str, expiresIn: str, expiresDate: str):
        self.status = status
        self.value = value
        self.customer = customer
        self.comment = comment
        self.paymentLinkID = paymentLinkID
        self.correlationID = correlationID
        self.paymentLinkUrl = paymentLinkUrl
        self.qrCodeImage = qrCodeImage
        self.brCode = brCode
        self.additionalInfo = additionalInfo
        
        self.expiresDate = expiresDate
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        self.expiresIn = expiresIn


class ChargeGet:
    def __init__(self, charge: Charge):
        self.charge = charge

class ChargeList:
    def __init__(self, pageInfo: PageInfo, charges: List[EasyCharge]):
        self.pageInfo = pageInfo
        self.charges = charges