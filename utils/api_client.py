import requests

BASE_URL = "https://petstore.swagger.io/v2"

class APIClient :
    def get (self, endpoint):
        return requests.get(f"{BASE_URL}{endpoint}")

    def post (self, endpoint, payload):
        return requests.post(f"{BASE_URL}{endpoint}",json = payload)
    
    def put (self, endpoint, payload):
        return requests.put(f"{BASE_URL}{endpoint}", json = payload)
    
    def delete(self, endpoint):
        return requests.delete(f"{BASE_URL}{endpoint}")