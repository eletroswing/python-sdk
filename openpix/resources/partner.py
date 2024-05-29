"""
    Module: partner
"""
from openpix.http import HttpClient
import partner_types

class Partner:
    """
    Access to Partner  

    [Click here for more info](https://developers.woovi.com/api#tag/partner-(request-access))  # pylint: disable=line-too-long
    """
    def __init__(self, HttpClient: HttpClient):
        self._client = HttpClient

    def get(self, taxID: str) -> partner_types.PartnerGet:
        return self._client.get(path=f'/api/v1/partner/company/{taxID}')


    def list(self, limit: int = 10, skip: int = 0) -> partner_types.PartnerList:
        return self._client.get(path=f'/api/v1/partner/company', query={"limit": limit, "skip": skip})

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