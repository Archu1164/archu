from fastapi import FastAPI

app=FastAPI()
@app.get("/xyz")
def read_root():
    return{"message":"Welcomeffsfdfesf to FastAPI!server is responding succesfully"}
@app.get("/23docs")
def get_docs():
    return{"docs_url":"http://127.0.0.1:8000/docs"}   

@app.post("/create-user")
def create_user(name:str,age:int):
    return{"message":"user created successfully!","name":name,"age":age}

@app.put("/update-user")
def update_user(user_id:int,name:str,age:int):
    return{
        "message":"user updatedn successfully!",
        "user_id":user_id,
        "updated_name":name,
        "updated_age":age
        
    }