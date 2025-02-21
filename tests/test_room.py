import pytest
from room import RoomAPI

@pytest.fixture
def room_api():
    return RoomAPI()

def test_create_room(room_api):
    result = room_api.create_room(1, 1, "Living Room", area="200 sqft")
    assert "room_name" in result
    assert result["room_name"] == "Living Room"

def test_read_room(room_api):
    # Pre-create the room before attempting to read it.
    room_api.create_room(1, 1, "Living Room", area="200 sqft")
    result = room_api.read_room(1, 1, "Living Room")
    assert "room_name" in result
    assert result["room_name"] == "Living Room"

def test_update_room(room_api):
    # Pre-create the room before updating it.
    room_api.create_room(1, 1, "Living Room", area="200 sqft")
    result = room_api.update_room(1, 1, "Living Room", area="250 sqft")
    assert "room_name" in result
    assert result["room_name"] == "Living Room"
    # Optionally verify that the metadata was updated
    assert result["updated_metadata"].get("area") == "250 sqft"

def test_delete_room(room_api):
    # Pre-create the room before deleting it.
    room_api.create_room(1, 1, "Living Room", area="200 sqft")
    result = room_api.delete_room(1, 1, "Living Room")
    assert result is True
