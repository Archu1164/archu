from fastapi import FastAPI

app = FastAPI()

# Example: http://127.0.0.1:8000/items?name=archana&age=25
@app.get("/items")
def get_item(name: str, age: int):
    return {
        "name": name,
        "age": age,
        "message": f"Hello {name}, you are {age} years old!"
    }