import pytest
from utils.api_client import APIClient
import random
from testdata.pet_payload import create_pet_payload 
from testdata.user_payload import create_user_payload
from testdata.order_payload import create_order_payload

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def pet_id():
    return random.randint(100000, 999999)

@pytest.fixture
def created_pet(api_client, pet_id):
    payload = create_pet_payload(pet_id)

    response = api_client.post("/pet", payload)
    assert response.status_code == 200

    return payload

@pytest.fixture
def created_user(api_client):
    payload = create_user_payload()
    
    response = api_client.post("/user",payload)
    assert response.status_code == 200

    return payload
    

@pytest.fixture
def created_order(api_client, pet_id):
    payload = create_order_payload(pet_id)

    response = api_client.post("/store/order/", payload)

    assert response.status_code == 200
    return payload