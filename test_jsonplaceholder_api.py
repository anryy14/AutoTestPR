import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def test_post():
    payload = {}
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == 201
    data = response.json()

def test_get():
    payload = {}
    response = requests.get(f"{BASE_URL}", json=payload)
    assert response.status_code == 200
    data = response.json()

def test_delete():
    response = requests.delete(f"{BASE_URL}/1")
    assert response.status_code == 200