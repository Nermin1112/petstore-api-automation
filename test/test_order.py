from testdata.order_payload import create_order_payload

def test_create_order(api_client,pet_id):

    payload = create_order_payload(pet_id)
    response = api_client.post("/store/order/", payload)

    assert response.status_code == 200

    get_response = api_client.get(f"/store/order/{payload['id']}")
    assert get_response.status_code == 200

    data = get_response.json()

    assert data["id"] == payload ["id"]
    assert data["petId"] == payload ["petId"]
    assert data["quantity"] == payload ["quantity"]
   


def test_delete_order(api_client,created_order):

    response = api_client.delete(f"/store/order/{created_order['id']}")

    assert response.status_code == 200


def test_get_nonexistent_order(api_client):
    response = api_client.get(f"/store/order/{9999999}")
  
    assert response.status_code == 404

def test_delete_nonexistent_order(api_client):
    response = api_client.delete(f"/store/order/{9999999}")
    
    assert response.status_code == 404