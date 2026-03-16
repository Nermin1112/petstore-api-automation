from faker import Faker
import random

fake = Faker()

def create_pet_payload(pet_id):
    return  {
        "id": pet_id,
        "name":fake.first_name(),
        "status" : "available"
        }
        
    
def update_pet_payloads(pet_id):
    return{
        "id": pet_id,
        "name":fake.first_name(),
        "status" : "available"
        }