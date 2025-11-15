# test_main.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_add_numbers():
    response = client.get("/add?a=2&b=3")
    data = response.json()
    
    assert response.status_code == 200
    assert data["result"] == 5
