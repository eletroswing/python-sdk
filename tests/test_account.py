# test_get.py
import pytest
import responses
from openpix.http import HttpClient
import openpix.resources.account as app

@pytest.fixture
def client():
    return HttpClient(app_id='123')

@pytest.fixture
def resource(client):
    return app(client)

@responses.activate
def test_should_get_error(resource):
    responses.add(
        responses.GET,
        'https://api.openpix.com.br/api/v1/account/some-id',
        json={'error': 'not exists'},
        status=400
    )

    with pytest.raises(Exception) as excinfo:
        resource({'id': 'some_id'})
    assert excinfo.value.args[0] == {'error': 'not exists'}

@responses.activate
def test_should_have_success(resource):
    account = {
        'account': {
            'accountId': '6290ccfd42831958a405debc',
            'isDefault': True,
            'balance': {
                'total': 129430,
                'blocked': 0,
                'available': 129430,
            },
        },
    }

    responses.add(
        responses.GET,
        'https://api.openpix.com.br/api/v1/account/some-id',
        json={'account': account},
        status=200
    )

    response = resource({'id': 'some_id'})
    assert response == {'account': account}
