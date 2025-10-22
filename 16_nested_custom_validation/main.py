# Nested models and custom validation
from fastapi import FastAPI
from pydantic import BaseModel, validator
from typing import List

class Address(BaseModel):
    city: str
    zip_code: str

class Customer(BaseModel):
    name: str
    addresses: List[Address]

    @validator('addresses')
    def check_addresses(cls, v):
        if not v:
            raise ValueError('At least one address required')
        return v

app = FastAPI()

@app.post("/customers/")
def create_customer(customer: Customer):
    return {"method": "POST", "customer": customer}

# GET - Get sample customer
@app.get("/customers/")
def get_customer():
    sample_customer = {
        "name": "Archana",
        "addresses": [
            {"city": "Hyderabad", "zip_code": "500001"},
            {"city": "Bangalore", "zip_code": "560001"}
        ]
    }
    return {"method": "GET", "customer": sample_customer}

# PUT - Update customer
@app.put("/customers/")
def update_customer(customer: Customer):
    return {"method": "PUT", "updated_customer": customer}
