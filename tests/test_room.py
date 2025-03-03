import pytest
from fastapi.testclient import TestClient
from server import app

# Create a test client for FastAPI
client = TestClient(app)

def test_create_room():
    # Ensure the house and floor exist before adding a room
    client.post("/houses/", json={"house_name": "My Home", "metadata": {}})
    client.post("/houses/My Home/floors/", json={"floor_number": 1, "metadata": {}})

    response = client.post(
        "/houses/My Home/floors/1/rooms/",
        json={"room_name": "Living Room", "metadata": {"area": "200 sqft"}}
    )
    assert response.status_code == 200
    result = response.json()
    assert "room_name" in result
    assert result["room_name"] == "Living Room"

def test_read_room():
    # Ensure the house, floor, and room exist before reading
    client.post("/houses/", json={"house_name": "My Home", "metadata": {}})
    client.post("/houses/My Home/floors/", json={"floor_number": 1, "metadata": {}})
    client.post("/houses/My Home/floors/1/rooms/", json={"room_name": "Living Room", "metadata": {"area": "200 sqft"}})

    response = client.get("/houses/My Home/floors/1/rooms/Living Room")
    assert response.status_code == 200
    result = response.json()
    assert "room_name" in result
    assert result["room_name"] == "Living Room"

def test_update_room():
    # Ensure the house, floor, and room exist before updating
    client.post("/houses/", json={"house_name": "My Home", "metadata": {}})
    client.post("/houses/My Home/floors/", json={"floor_number": 1, "metadata": {}})
    client.post("/houses/My Home/floors/1/rooms/", json={"room_name": "Living Room", "metadata": {"area": "200 sqft"}})

    response = client.put("/houses/My Home/floors/1/rooms/Living Room", json={"metadata": {"area": "250 sqft"}})
    assert response.status_code == 200
    result = response.json()
    assert "room_name" in result
    assert result["room_name"] == "Living Room"
    assert result["metadata"].get("area") == "250 sqft"

def test_delete_room():
    # Ensure the house, floor, and room exist before deleting
    client.post("/houses/", json={"house_name": "My Home", "metadata": {}})
    client.post("/houses/My Home/floors/", json={"floor_number": 1, "metadata": {}})
    client.post("/houses/My Home/floors/1/rooms/", json={"room_name": "Living Room", "metadata": {"area": "200 sqft"}})

    response = client.delete("/houses/My Home/floors/1/rooms/Living Room")
    assert response.status_code == 200
    result = response.json()
    assert result["message"] == "Room 'Living Room' deleted from floor '1' in house 'My Home'"
