from faker import Faker
import random

fake = Faker() 

def create_user_payload():
    return  {
        "id": random.randint(100000, 999999),
        "username": fake.user_name(),
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "email": fake.email(),
        "password": fake.password(length=10),
        "phone": fake.phone_number(),
        "userStatus": random.randint(0, 1)
        }


    


 