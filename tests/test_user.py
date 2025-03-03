import pytest
from fastapi.testclient import TestClient
from server import app

# Create a test client for FastAPI
client = TestClient(app)

def test_create_user():
    response = client.post(
        "/users/",
        json={"username": "john_doe", "attributes": {"email": "john@example.com"}}
    )
    assert response.status_code == 200
    result = response.json()
    assert "username" in result
    assert result["username"] == "john_doe"

def test_read_user():
    # Create a user before reading it
    create_response = client.post("/users/", json={"username": "john_doe", "attributes": {"email": "john@example.com"}})
    user_id = create_response.json()["user_id"]

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    result = response.json()
    assert "user_id" in result
    assert result["user_id"] == user_id

def test_update_user():
    # Create a user before updating it
    create_response = client.post("/users/", json={"username": "john_doe", "attributes": {"email": "john@example.com"}})
    user_id = create_response.json()["user_id"]

    response = client.put(f"/users/{user_id}", json={"attributes": {"email": "john_new@example.com"}})
    assert response.status_code == 200
    result = response.json()
    assert "user_id" in result
    assert result["user_id"] == user_id
    assert result["attributes"].get("email") == "john_new@example.com"

def test_delete_user():
    # Create a user before deleting it
    create_response = client.post("/users/", json={"username": "john_doe", "attributes": {"email": "john@example.com"}})
    user_id = create_response.json()["user_id"]

    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200
    result = response.json()
    assert result["message"] == f"User {user_id} deleted successfully"
