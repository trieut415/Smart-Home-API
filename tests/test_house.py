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
    result = house_api.read_house(1)
    assert "house_id" in result
    assert result["house_id"] == 1

def test_update_house(house_api):
    result = house_api.update_house(1, owner="John Doe")
    assert "house_id" in result
    assert result["house_id"] == 1

def test_delete_house(house_api):
    result = house_api.delete_house(1)
    assert result is True

def test_add_floor(house_api):
    result = house_api.add_floor(1, 1, description="First Floor")
    assert "floor_number" in result
    assert result["floor_number"] == 1

def test_delete_floor(house_api):
    result = house_api.delete_floor(1, 1)
    assert result is True
