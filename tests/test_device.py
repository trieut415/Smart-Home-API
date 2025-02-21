import pytest
from device import DeviceAPI

@pytest.fixture
def device_api():
    return DeviceAPI()

def test_create_device(device_api):
    result = device_api.create_device("dev001", "Thermostat", brand="SmartCo")
    assert "device_id" in result
    assert result["device_id"] == "dev001"

def test_read_device(device_api):
    # Pre-create the device before attempting to read it.
    device_api.create_device("dev001", "Thermostat", brand="SmartCo")
    result = device_api.read_device("dev001")
    assert "device_id" in result
    assert result["device_id"] == "dev001"

def test_update_device(device_api):
    # Pre-create the device before updating.
    device_api.create_device("dev001", "Thermostat", brand="SmartCo")
    result = device_api.update_device("dev001", brand="SmartCo Pro")
    assert "device_id" in result
    assert result["device_id"] == "dev001"
    # Optionally, check that the updated metadata contains the new value.
    assert result["updated_metadata"].get("brand") == "SmartCo Pro"

def test_assign_device(device_api):
    # Pre-create the device before assigning it.
    device_api.create_device("dev001", "Thermostat", brand="SmartCo")
    result = device_api.assign_device("dev001", location_type="room", location_identifier="Living Room")
    assert "device_id" in result
    assert result["device_id"] == "dev001"
    assert "assigned_to" in result
    # Depending on your implementation, the key in the assigned_to dict might be 'room'
    assert result["assigned_to"].get("room") == "Living Room"

def test_delete_device(device_api):
    # Pre-create the device before deleting it.
    device_api.create_device("dev001", "Thermostat", brand="SmartCo")
    result = device_api.delete_device("dev001")
    assert result is True
