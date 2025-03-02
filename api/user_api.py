from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Dict, Optional, Any

router = APIRouter()

# In-memory storage for users
users = {}
next_user_id = 1  # Auto-incremented user ID

# Pydantic Models
class UserCreate(BaseModel):
    username: str = Field(..., description="Unique username")
    attributes: Optional[Dict[str, Any]] = Field(default_factory=dict)

class UserUpdate(BaseModel):
    attributes: Dict[str, Any] = Field(..., description="Updated attributes for the user")

class UserResponse(BaseModel):
    user_id: int
    username: str
    attributes: Dict[str, Any]

# API Endpoints

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate):
    global next_user_id
    user_id = next_user_id
    next_user_id += 1

    new_user = {
        "user_id": user_id,
        "username": user.username,
        "attributes": user.attributes
    }
    users[user_id] = new_user
    return new_user

@router.get("/{user_id}", response_model=UserResponse)
def read_user(user_id: int):
    user = users.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, update: UserUpdate):
    user = users.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user["attributes"].update(update.attributes)
    return user

@router.delete("/{user_id}")
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    del users[user_id]
    return {"message": f"User {user_id} deleted successfully"}
