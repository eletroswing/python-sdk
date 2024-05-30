from openpix.types import PageInfo
from typing import List

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
    def __init__(self, name: str, email: str, phone: str, taxID: TaxID, address: Address):
        self.name = name
        self.email = email
        self.phone = phone
        self.taxID = taxID
        self.address = address

class AdditionalInfo:
    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value

class PixQrCode:
    def __init__(self, name: str, value: str, comment: str, brCode: str, correlationID: str, 
                 paymentLinkID: str, paymentLinkUrl: str, qrCodeImage: str, createdAt: str, updatedAt: str):
        self.name = name
        self.value = value
        self.comment = comment
        self.brCode = brCode
        self.correlationID = correlationID
        self.paymentLinkID = paymentLinkID
        self.paymentLinkUrl = paymentLinkUrl
        self.qrCodeImage = qrCodeImage
        self.createdAt = createdAt
        self.updatedAt = updatedAt

class Charge:
    def __init__(self, value: int, customer: Customer, type: str, comment: str, brCode: str, status: str, correlationID: str, 
                 paymentLinkID: str, paymentLinkUrl: str, globalID: str, transactionID: str, identifier: str, qrCodeImage: str, 
                 additionalInfo: list, pixKey: str, createdAt: str, updatedAt: str, expiresIn: str):
        self.value = value
        self.customer = customer
        self.type = type
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

class Subscription:
    def __init__(self, globalID: str, value: int, customer: Customer, dayGenerateCharge: int, status: str, correlationID: str):
        self.globalID = globalID
        self.value = value
        self.customer = customer
        self.dayGenerateCharge = dayGenerateCharge
        self.status = status
        self.correlationID = correlationID

class Transaction:
    def __init__(self, charge: Charge, value: int, time: str, endToEndID: str, transactionID: str, infoPagador: str, 
                 customer: Customer, withdraw: dict, payer: Customer, type: str, globalID: str, pixQrCode: PixQrCode):
        self.charge = charge
        self.value = value
        self.time = time
        self.endToEndID = endToEndID
        self.transactionID = transactionID
        self.infoPagador = infoPagador
        self.customer = customer
        self.withdraw = withdraw
        self.payer = payer
        self.type = type
        self.globalID = globalID
        self.pixQrCode = pixQrCode
        
class TransactionsGet:
    def __init__(self, transaction: Transaction):
        self.transaction = transaction

class TransactionsList: 
    def __init__(self, pageInfo: PageInfo, transactions: List[Transaction]):
        self.pageInfo = pageInfo
        self.transactions = transactions
