import pytest
import requests
from credetials.creds import *

base_url = "http://localhost:8000/api"

@pytest.fixture
def api_client():
    return requests.Session()

def test_login(api_client):
    login_data = {
        'email': email,
        'password': password
    }
    response = api_client.post(f"{base_url}/login", data=login_data)
    assert response.status_code == 200
    token = response.json().get('token')
    assert token is not None
    return token

def authenticated_client(api_client, test_login):
    api_client.headers.update({'Authorization': f"Bearer {test_login}"})
    return api_client