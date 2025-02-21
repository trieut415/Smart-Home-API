import pytest
from user import UserAPI

@pytest.fixture
def user_api():
    return UserAPI()

def test_create_user(user_api):
    result = user_api.create_user("john_doe", email="john@example.com")
    assert "username" in result
    assert result["username"] == "john_doe"

def test_read_user(user_api):
    # Pre-create a user before reading
    user = user_api.create_user("john_doe", email="john@example.com")
    result = user_api.read_user(user["user_id"])
    assert "user_id" in result
    assert result["user_id"] == user["user_id"]

def test_update_user(user_api):
    # Pre-create a user before updating
    user = user_api.create_user("john_doe", email="john@example.com")
    result = user_api.update_user(user["user_id"], email="john_new@example.com")
    assert "user_id" in result
    assert result["user_id"] == user["user_id"]
    # Verify that the updated attributes include the new email
    assert result["updated_attributes"].get("email") == "john_new@example.com"

def test_delete_user(user_api):
    # Pre-create a user before deleting
    user = user_api.create_user("john_doe", email="john@example.com")
    result = user_api.delete_user(user["user_id"])
    assert result is True
