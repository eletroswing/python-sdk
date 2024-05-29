"""
    Module: customer
"""
from openpix.http import HttpClient

import charge_types

class Customer:
    """
    Access to Customer  

    [Click here for more info](https://developers.woovi.com/api#tag/customer)  # pylint: disable=line-too-long
    """
    def __init__(self, HttpClient: HttpClient):
        self._client = HttpClient

    def get(self, id: str) -> charge_types.CustomerGet:
        return self._client.get(path=f'/api/v1/customer/{id}')

    def list(self, limit: int = 10, skip: int = 0) -> charge_types.ChargeList:
        return self._client.get(path=f'/api/v1/customer', query={"limit": limit, "skip": skip})

    def create(self, name: str, email: str, phone: str, taxID: str, address: charge_types.Address) -> charge_types.CustomerCreate:
        return self._client.post(path=f'/api/v1/customer', data={
            'name': name,
            'phone': phone,
            'taxID': taxID,
            'email': email,
            'address': {
                'zipcode': address.zipcode,	
                'street': address.street,	
                'number': address.number,	
                'neighborhood': address.neighborhood,	
                'city': address.city,	
                'state': address.state,	
                'complement': address.complement,	
                'country': address.country,	
            }
        })
    
    def update(self, correlationID: str, name: str, email: str, phone: str, taxID: str, address: charge_types.Address) -> charge_types.CustomerUpdate:
        return self._client.patch(path=f'/api/v1/customer/{correlationID}', data={
            'name': name,
            'phone': phone,
            'taxID': taxID,
            'email': email,
            'address': {
                'zipcode': address.zipcode,	
                'street': address.street,	
                'number': address.number,	
                'neighborhood': address.neighborhood,	
                'city': address.city,	
                'state': address.state,	
                'complement': address.complement,	
                'country': address.country,	
            }
        })
        