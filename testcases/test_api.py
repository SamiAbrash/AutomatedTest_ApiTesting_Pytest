import pytest
import requests

base_url = "http://localhost:8000/api"

@pytest.fixture
def api_client():
    return requests.Session()

def test_all_books(api_client):
    response = api_client.get(f"{base_url}/books")
    assert response.status_code == 200
    assert isinstance(response.json(), list)