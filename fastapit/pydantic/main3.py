from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None
    origin: str


items_db = {}


class Student(BaseModel):
    name: str
    age: int
    grade: str

@app.get("/students/")
def get_all_students():
    return [
        {"name": "Archu", "age": 21, "grade": "A++"},
        {"name": "Bunny", "age": 17, "grade": "B++"}
    ]


@app.get("/items/")
def get_all_items():
    return list(items_db.values())


@app.post("/items/")
def create_item(item: Item):
    items_db[item.name] = item
    return item


@app.get("/items/{name}")
def get_item(name: str):
    item = items_db.get(name)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.put("/items/{name}")
def update_item(name: str, item: Item):
    if name not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[name] = item
    return item
