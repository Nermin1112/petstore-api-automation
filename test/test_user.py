from testdata.user_payload import create_user_payload
import json


def test_create_user(api_client):

    payload = create_user_payload()
    response = api_client.post(f"/user", payload)

    assert response.status_code == 200

    get_response = api_client.get(f"/user/{payload['username']}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["username"] == payload["username"]
    assert data["email"] == payload["email"]


def test_delete_user(api_client, created_user):
    
    response = api_client.delete(f"/user/{created_user['username']}")
    assert response.status_code == 200

def test_get_nonexistent_user(api_client):

    response = api_client.get("/user/user_99999")

    assert response.status_code == 404

def test_delete_user_and_verify(api_client, created_user):

    response = api_client.delete(f"/user/{created_user['username']}")

    assert response.status_code == 200

    verify_response = api_client.get(f"/user/{created_user['username']}")

    assert verify_response.status_code == 404
