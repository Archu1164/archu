from fastapi import FastAPI
app=FastAPI()

@app.get("/hello")
def say_hello():
    return{"message":"Hello World"}

@app.get("/docs-url")
def get_docs():
    return {"docs_url":"http://127.0.0.1:8000/docs"}
@app.post("/create")
def create_item(name:str):
    return{"message":"Item created","name":name}

@app.put("/update")
def update_item(name:str):
    return{"message":"Item updated","name":name}

@app.delete("/delete")
def delete_item(item_id:int):
    return{"message":"Item deleted","id":item_id}