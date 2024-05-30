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

class Subscription:
    def __init__(self, globalID: str, value: int, customer: Customer, dayGenerateCharge: int, status: str, correlationID: str):
        self.globalID = globalID
        self.value = value
        self.customer = customer
        self.dayGenerateCharge = dayGenerateCharge
        self.status = status
        self.correlationID = correlationID

class AditionalInfo:
    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value

class SubscriptionGet:
    def __init__(self, subscription: Subscription):
        self.subscription = subscription

class SubscriptionCreate:
    def __init__(self, subscription: Subscription):
        self.subscription = subscription
