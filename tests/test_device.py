import pytest
from api.device_api import router as device_router
from fastapi.testclient import TestClient
from server import app

# Create a test client for FastAPI
client = TestClient(app)

def test_create_device():
    response = client.post(
        "/devices/",
        json={"device_id": "dev001", "device_type": "Thermostat", "metadata": {"brand": "SmartCo"}}
    )
    assert response.status_code == 200
    result = response.json()
    assert "device_id" in result
    assert result["device_id"] == "dev001"

def test_read_device():
    # Ensure the device is created before reading
    client.post("/devices/", json={"device_id": "dev001", "device_type": "Thermostat", "metadata": {"brand": "SmartCo"}})
    
    response = client.get("/devices/dev001")
    assert response.status_code == 200
    result = response.json()
    assert "device_id" in result
    assert result["device_id"] == "dev001"

def test_update_device():
    # Create the device first
    client.post("/devices/", json={"device_id": "dev001", "device_type": "Thermostat", "metadata": {"brand": "SmartCo"}})

    response = client.put("/devices/dev001", json={"metadata": {"brand": "SmartCo Pro"}})
    assert response.status_code == 200
    result = response.json()
    assert "device_id" in result
    assert result["device_id"] == "dev001"
    assert result["metadata"].get("brand") == "SmartCo Pro"

def test_assign_device():
    # Create the device first
    client.post("/devices/", json={"device_id": "dev001", "device_type": "Thermostat", "metadata": {"brand": "SmartCo"}})

    response = client.post("/devices/dev001/assign", json={"location_type": "room", "location_identifier": "Living Room"})
    assert response.status_code == 200
    result = response.json()
    assert "device_id" in result
    assert result["device_id"] == "dev001"
    assert result["assigned_to"]["room"] == "Living Room"

def test_delete_device():
    # Create the device first
    client.post("/devices/", json={"device_id": "dev001", "device_type": "Thermostat", "metadata": {"brand": "SmartCo"}})

    response = client.delete("/devices/dev001")
    assert response.status_code == 200
    result = response.json()
    assert result["message"] == "Device dev001 deleted successfully"
