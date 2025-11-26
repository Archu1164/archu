#complete crud operations
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Pydantic Model
class User(BaseModel):
    id: int
    name: str
    age: int

# In-memory storage
users_db = []


# CREATE
@app.post("/users")
def create_user(user: User):
    users_db.append(user)
    return {"message": "User created", "data": user}


# READ ALL
@app.get("/users")
def get_users():
    return users_db


# READ ONE
@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")
