import pytest
from house import HouseAPI

@pytest.fixture
def house_api():
    return HouseAPI()

def test_create_house(house_api):
    result = house_api.create_house("My Home", location="123 Main St")
    assert "house_name" in result
    assert result["house_name"] == "My Home"

def test_read_house(house_api):
    # Pre-create the house before reading it.
    house_api.create_house("My Home", location="123 Main St")
    result = house_api.read_house("My Home")
    assert "house_name" in result
    assert result["house_name"] == "My Home"

def test_update_house(house_api):
    # Pre-create the house before updating.
    house_api.create_house("My Home", location="123 Main St")
    result = house_api.update_house("My Home", owner="John Doe")
    # Our update returns 'house_id' instead of 'house_name'
    assert "house_id" in result
    assert result["house_id"] == "My Home"
    # Ensure that the metadata update took effect.
    assert result["updated_metadata"].get("owner") == "John Doe"

def test_delete_house(house_api):
    # Pre-create the house before deleting.
    house_api.create_house("My Home", location="123 Main St")
    result = house_api.delete_house("My Home")
    assert result is True

def test_add_floor(house_api):
    # Pre-create the house before adding a floor.
    house_api.create_house("My Home", location="123 Main St")
    result = house_api.add_floor("My Home", 1, description="First Floor")
    assert "floor_number" in result
    assert result["floor_number"] == 1

def test_delete_floor(house_api):
    # Pre-create the house and add a floor before deleting it.
    house_api.create_house("My Home", location="123 Main St")
    house_api.add_floor("My Home", 1, description="First Floor")
    result = house_api.delete_floor("My Home", 1)
    assert result is True
