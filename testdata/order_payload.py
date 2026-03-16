from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

def create_order_payload(pet_id):
    return  {"id": random.randint(100000, 999999),
             "petId": pet_id,
             "quantity": random.randint(0, 7),
             "shipDate": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%S"),
             "status": "placed",
             "complete": True
  }
