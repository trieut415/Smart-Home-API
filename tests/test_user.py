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
    result = user_api.read_user(1)
    assert "user_id" in result
    assert result["user_id"] == 1

def test_update_user(user_api):
    result = user_api.update_user(1, email="john_new@example.com")
    assert "user_id" in result
    assert result["user_id"] == 1

def test_delete_user(user_api):
    result = user_api.delete_user(1)
    assert result is True
