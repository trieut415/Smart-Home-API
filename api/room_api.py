from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Dict, Optional, Any

router = APIRouter()

# In-memory storage for rooms
rooms = {}  # { house_id: { floor_number: { room_name: room_data } } }

# Pydantic Models
class RoomCreate(BaseModel):
    room_name: str = Field(..., description="Unique name of the room")
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)

class RoomUpdate(BaseModel):
    metadata: Dict[str, Any] = Field(..., description="Updated metadata for the room")

class RoomResponse(BaseModel):
    house_id: str
    floor_number: int
    room_name: str
    metadata: Dict[str, Any]

# API Endpoints

@router.post("/{house_id}/floors/{floor_number}/rooms/", response_model=RoomResponse)
def create_room(house_id: str, floor_number: int, room: RoomCreate):
    # Ensure house entry exists
    if house_id not in rooms:
        rooms[house_id] = {}
    # Ensure floor entry exists for the house
    if floor_number not in rooms[house_id]:
        rooms[house_id][floor_number] = {}
    # Check if room already exists
    if room.room_name in rooms[house_id][floor_number]:
        raise HTTPException(status_code=400, detail=f"Room '{room.room_name}' already exists on floor '{floor_number}' in house '{house_id}'.")

    new_room = {
        "house_id": house_id,
        "floor_number": floor_number,
        "room_name": room.room_name,
        "metadata": room.metadata
    }
    rooms[house_id][floor_number][room.room_name] = new_room
    return new_room

@router.get("/{house_id}/floors/{floor_number}/rooms/{room_name}", response_model=RoomResponse)
def read_room(house_id: str, floor_number: int, room_name: str):
    try:
        return rooms[house_id][floor_number][room_name]
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Room '{room_name}' on floor '{floor_number}' in house '{house_id}' not found.")

@router.put("/{house_id}/floors/{floor_number}/rooms/{room_name}", response_model=RoomResponse)
def update_room(house_id: str, floor_number: int, room_name: str, update: RoomUpdate):
    try:
        room = rooms[house_id][floor_number][room_name]
        room["metadata"].update(update.metadata)
        return room
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Room '{room_name}' on floor '{floor_number}' in house '{house_id}' not found.")

@router.delete("/{house_id}/floors/{floor_number}/rooms/{room_name}")
def delete_room(house_id: str, floor_number: int, room_name: str):
    try:
        del rooms[house_id][floor_number][room_name]
        return {"message": f"Room '{room_name}' deleted from floor '{floor_number}' in house '{house_id}'"}
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Room '{room_name}' on floor '{floor_number}' in house '{house_id}' does not exist.")
