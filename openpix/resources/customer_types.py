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
    def __init__(self, name: str, email: str, phone: str, taxID: TaxID, correlationID: str, address: Address):
        self.name = name
        self.email = email
        self.phone = phone
        self.taxID = taxID
        self.correlationID = correlationID
        self.address = address

class CustomerGet:
    def __init__(self, customer: Customer):
        self.customer = customer

class CustomerUpdate:
    def __init__(self, customer: Customer):
        self.customer = customer

class CustomerCreate:
    def __init__(self, customer: Customer):
        self.customer = customer

class CustomerList: 
    def __init__(self, pageInfo: PageInfo, customers: List[Customer]):
        self.pageInfo = pageInfo
        self.customers = customers
