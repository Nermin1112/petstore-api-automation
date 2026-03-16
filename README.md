

# Petstore API Automation Tests

Automated API testing project for the Swagger Petstore API using Python, Pytest, and Requests.

## Project Overview

This project demonstrates automated API testing for the Swagger Petstore API. 
The goal is to validate core CRUD operations for pets, users, and orders using automated tests.

The project follows a clean and scalable automation structure using fixtures, reusable API clients, and separated test data.

The project is structured using reusable API client utilities, pytest fixtures for test setup, and dynamically generated test data using Faker.

## Tech Stack

- Python
- Pytest
- Requests
- Faker
- Pytest Fixtures

## API Under Test

Swagger Petstore API: https://petstore.swagger.io/

## Project Structure

```
petstore-api-automation
│
├── test
│   ├── test_pet.py
│   ├── test_user.py
│   └── test_order.py
│
├── utils
│   └── api_client.py
│
├── testdata
│   ├── pet_payloads.py
│   ├── user_payloads.py
│   └── order_payloads.py
│
├── conftest.py
├── requirements.txt
├── pytest.ini
├── .gitignore
└── README.md


## Test Coverage

### Pet endpoints
- Create pet
- Get pet by ID
- Update pet
- Delete pet
- Delete pet twice
- Invalid pet ID
- Empty request body

### User endpoints
- Create user
- Get user
- Delete user
- Non-existing user

### Order endpoints
- Create order
- Get order
- Delete order
- Non-existing order

## Running the Tests

Install dependencies:

pip install -r requirements.txt

Run tests:

pytest -v

## Notes

During testing it was observed that some Petstore endpoints return HTTP 200 even for invalid input values.

This behaviour appears to be a validation issue in the API and has been documented within the tests