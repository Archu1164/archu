#post endpoint with pydantic
from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class User(BaseModel):
    
    name:str
    age:int
@app.post("/users")
def create_user(user:User):
  return{"data":user}    