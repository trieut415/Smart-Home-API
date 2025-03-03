import pytest
from fastapi.testclient import TestClient
from server import app

# Create a test client for FastAPI
client = TestClient(app)

def test_create_house():
    response = client.post(
        "/houses/",
        json={"house_name": "My Home", "metadata": {"location": "123 Main St"}}
    )
    assert response.status_code == 200
    result = response.json()
    assert "house_name" in result
    assert result["house_name"] == "My Home"

def test_read_house():
    # Ensure the house is created before reading
    client.post("/houses/", json={"house_name": "My Home", "metadata": {"location": "123 Main St"}})
    
    response = client.get("/houses/My Home")
    assert response.status_code == 200
    result = response.json()
    assert "house_name" in result
    assert result["house_name"] == "My Home"

def test_update_house():
    # Create the house first
    client.post("/houses/", json={"house_name": "My Home", "metadata": {"location": "123 Main St"}})

    response = client.put("/houses/My Home", json={"metadata": {"owner": "John Doe"}})
    assert response.status_code == 200
    result = response.json()
    assert "house_name" in result
    assert result["house_name"] == "My Home"
    assert result["metadata"].get("owner") == "John Doe"

def test_delete_house():
    # Create the house first
    client.post("/houses/", json={"house_name": "My Home", "metadata": {"location": "123 Main St"}})

    response = client.delete("/houses/My Home")
    assert response.status_code == 200
    result = response.json()
    assert result["message"] == "House 'My Home' deleted successfully"

def test_add_floor():
    # Create the house first
    client.post("/houses/", json={"house_name": "My Home", "metadata": {"location": "123 Main St"}})

    response = client.post("/houses/My Home/floors/", json={"floor_number": 1, "metadata": {"description": "First Floor"}})
    assert response.status_code == 200
    result = response.json()
    assert "floors" in result
    assert "1" in result["floors"]  # Ensure key is an integer

def test_delete_floor():
    # Create the house first
    client.post("/houses/", json={"house_name": "My Home", "metadata": {"location": "123 Main St"}})
    client.post("/houses/My Home/floors/", json={"floor_number": 1, "metadata": {"description": "First Floor"}})

    response = client.delete("/houses/My Home/floors/1")
    assert response.status_code == 200
    result = response.json()
    assert result["message"] == "Floor '1' deleted from house 'My Home'"
