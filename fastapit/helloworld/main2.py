from fastapi import FastAPI
app=FastAPI()

@app.get("/items")
def get_items(limit: int=10,search:str=None):
    return{"limit":limit,"search":search}