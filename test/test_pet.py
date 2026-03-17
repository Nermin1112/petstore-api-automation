from testdata.pet_payload import create_pet_payload, update_pet_payload
from testdata.user_payload import create_user_payload


def test_create_pet(api_client, pet_id):

    payload = create_pet_payload(pet_id)

    response = api_client.post("/pet", payload)

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == payload["id"]
    assert data["name"] == payload["name"]
    assert data["status"] == payload["status"]

def test_create_pet_invalid_id(api_client):
    payload = create_pet_payload(-1)
    response = api_client.post("/pet", payload)

    #API bug: should return 400
    assert response.status_code == 200
    
    # Known issue: Swagger Petstore API currently accepts negative IDs and returns 200 OK
    # Logically, the API should return 400 Bad Request for invalid ID

def test_id_check(api_client, created_pet):

    response = api_client.get(f"/pet/{created_pet['id']}")
    data = response.json()

    assert response.status_code == 200
    assert data["id"] == created_pet["id"]
    assert data["name"] == created_pet["name"]
    assert data["status"] == created_pet["status"]



def test_edit_pet_name(api_client, created_pet):

    payload = update_pet_payload(created_pet['id'])

    response = api_client.put("/pet", payload)

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == payload["id"]
    assert data["name"] == payload["name"]
    assert data["status"] == payload["status"]

    get_response = api_client.get(f"/pet/{payload['id']}")
    data = get_response.json()
    assert data["name"] == payload["name"]

def test_delete_pet_id(api_client, created_pet):
    
    response = api_client.delete(f"/pet/{created_pet['id']}")

    assert response.status_code == 200

    verify_response = api_client.get(f"/pet/{created_pet['id']}")

    assert verify_response.status_code == 404

def test_delete_pet_twice(api_client, created_pet):

    response = api_client.delete(f"/pet/{created_pet['id']}")

    assert response.status_code == 200

    response = api_client.delete(f"/pet/{created_pet['id']}")

    assert response.status_code == 404

def test_empty_body(api_client):

    payload = {}
    response = api_client.post("/pet", payload)

    assert response.status_code == 200

    # Known issue: API accepts empty body (should return 400)





