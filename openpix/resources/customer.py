"""
    Module: customer
"""
from openpix.http import HttpClient
from openpix.types import PagePayload
import charge_types

class Customer:
    """
    Access to Customer  

    [Click here for more info](https://developers.woovi.com/api#tag/customer)  # pylint: disable=line-too-long
    """
    def __init__(self, HttpClient: HttpClient):
        self._client = HttpClient

    """get a customer
    Args:
        id (str): identifier of your customer.

        [Click here for more info](https://developers.openpix.com.br/api#tag/customer/paths/~1api~1v1~1customer~1%7Bid%7D/get)
    """
    def get(self, id: str) -> charge_types.CustomerGet:
        return self._client.get(path=f'/api/v1/customer/{id}')

    """list customers
    Args:
        page (PageInfo): A class for page info object containing limit and skip
    
        [Click here for more info](https://developers.openpix.com.br/api#tag/customer/paths/~1api~1v1~1customer~1%7Bid%7D/get)
    """
    def list(self, page: PagePayload = PagePayload()) -> charge_types.ChargeList:
        return self._client.get(path=f'/api/v1/customer', query={"limit": page.limit, "skip": page.skip})

    """create a customer
    Args:
        name (str): name of the customer.
        email (str): email of the customer.
        phone (str): phone number of your customer.
        taxID (str): personal document of your customer.
        correlationID (str): Your correlation ID, unique identifier refund.
        address (Address): 
            - zipcode: string
            - street: string
            - number: string
            - neighborhood: string
            - city: string
            - state: string
            - complement: string
            - country: string
    
        [Click here for more info](https://developers.openpix.com.br/api#tag/customer/paths/~1api~1v1~1customer/post)
    """
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
    
    """update a customer
    Args:
        correlationID (str): Your correlation ID, unique identifier refund.
        name (str): name of the customer.
        email (str): email of the customer.
        phone (str): phone number of your customer.
        taxID (str): personal document of your customer.
        address (Address): 
            - zipcode: string
            - street: string
            - number: string
            - neighborhood: string
            - city: string
            - state: string
            - complement: string
            - country: string
    
        [Click here for more info](https://developers.openpix.com.br/api#tag/customer/paths/~1api~1v1~1customer/post)
    """
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
        