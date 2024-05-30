"""
    Module: partner
"""
from openpix.http import HttpClient
import openpix.resources.partner_types as partner_types
from openpix.types import PagePayload

class Partner:
    """
    Access to Partner  

    [Click here for more info](https://developers.woovi.com/api#tag/partner-(request-access))  # pylint: disable=line-too-long
    """
    def __init__(self, HttpClient: HttpClient):
        self._client = HttpClient

    """Get an specific preregistration via taxID param.
    Args:
        taxID (str): The raw tax ID from the preregistration that you want to get
    
        [Click here for more info](https://developers.openpix.com.br/api#tag/partner-(request-access)/paths/~1api~1v1~1partner~1company~1%7BtaxID%7D/get)
    """
    def get(self, taxID: str) -> partner_types.PartnerGet:
        return self._client.get(path=f'/api/v1/partner/company/{taxID}')

    """Get every preregistration that is managed by you.
    Args:
        page (PageInfo): A class for page info object containing limit and skip
    
        [Click here for more info](https://developers.openpix.com.br/api#tag/partner-(request-access)/paths/~1api~1v1~1partner~1company/get)
    """
    def list(self, page: PagePayload = PagePayload()) -> partner_types.PartnerList:
        return self._client.get(path=f'/api/v1/partner/company', query={"limit": page.limit, "skip": page.skip})

    """Create a pre registration with a partner reference (your company)
    Args:
        preRegistration (preRegistration):
          - name: str
          - website: str
          - taxID: 
            - taxID: str
            - type: str

        user (user):
          - firstName: str
          - lastName: str
          - email: str
          - phone: str
    
        [Click here for more info](https://developers.openpix.com.br/api#tag/partner-(request-access)/paths/~1api~1v1~1partner~1company/post)
    """
    def createPreRegistration(self, preRegistration: partner_types.PreRegistrationCreate, user: partner_types.PreRegistrationUserObject):
        return self._client.post(path=f'/api/v1/partner/company', data={
          "preRegistration": {
            "name": preRegistration.name,
            "taxID": {
              "taxID": preRegistration.taxID.taxID,
              "type": preRegistration.taxID.type
            },
            "website": preRegistration.website
          },
          "user": {
            "firstName": user.firstName,
            "lastName": user.lastName,
            "email": user.email,
            "phone": user.phone
          }
        })

    """Create a new application to some of your preregistration's company.
    Args:
        application (application):
          - name: str
          - type: str

        taxID (taxID):
          - taxID: str
          - type: str
    
        [Click here for more info](https://developers.openpix.com.br/api#tag/partner-(request-access)/paths/~1api~1v1~1partner~1application/post)
    """
    def createApplication(self, application: partner_types.Application, taxID: partner_types.TaxId):
        return self._client.post(path=f'/api/v1/partner/application', data={
          "application": {
            "name": application.name,
            "type": application.type
          },
          "taxID": {
            "taxID": taxID.taxID,
            "type": taxID.type
            
          }
        })