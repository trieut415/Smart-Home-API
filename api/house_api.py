from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Dict, Optional, Any

router = APIRouter()

# In-memory storage for houses
houses = {}

# Pydantic Models
class HouseCreate(BaseModel):
    house_name: str = Field(..., description="Unique name of the house")
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HouseUpdate(BaseModel):
    metadata: Dict[str, Any] = Field(..., description="Updated metadata for the house")

class FloorCreate(BaseModel):
    floor_number: int = Field(..., description="Floor number to add")
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)

class HouseResponse(BaseModel):
    house_name: str
    metadata: Dict[str, Any]
    floors: Dict[int, Dict[str, Any]]

# API Endpoints

@router.post("/", response_model=HouseResponse)
def create_house(house: HouseCreate):
    if house.house_name in houses:
        raise HTTPException(status_code=400, detail="House already exists")
    
    new_house = {
        "house_name": house.house_name,
        "metadata": house.metadata,
        "floors": {}
    }
    houses[house.house_name] = new_house
    return new_house

@router.get("/{house_id}", response_model=HouseResponse)
def read_house(house_id: str):
    house = houses.get(house_id)
    if not house:
        raise HTTPException(status_code=404, detail="House not found")
    return house

@router.put("/{house_id}", response_model=HouseResponse)
def update_house(house_id: str, update: HouseUpdate):
    house = houses.get(house_id)
    if not house:
        raise HTTPException(status_code=404, detail="House not found")
    
    house["metadata"].update(update.metadata)
    return house

@router.delete("/{house_id}")
def delete_house(house_id: str):
    if house_id not in houses:
        raise HTTPException(status_code=404, detail="House not found")
    
    del houses[house_id]
    return {"message": f"House '{house_id}' deleted successfully"}

@router.post("/{house_id}/floors/", response_model=HouseResponse)
def add_floor(house_id: str, floor: FloorCreate):
    house = houses.get(house_id)
    if not house:
        raise HTTPException(status_code=404, detail="House not found")
    
    if floor.floor_number in house["floors"]:
        raise HTTPException(status_code=400, detail="Floor already exists")
    
    house["floors"][floor.floor_number] = {"floor_number": floor.floor_number, "metadata": floor.metadata, "rooms": {}}
    return house

@router.delete("/{house_id}/floors/{floor_number}")
def delete_floor(house_id: str, floor_number: int):
    house = houses.get(house_id)
    if not house:
        raise HTTPException(status_code=404, detail="House not found")
    
    if floor_number not in house["floors"]:
        raise HTTPException(status_code=404, detail="Floor not found")
    
    del house["floors"][floor_number]
    return {"message": f"Floor '{floor_number}' deleted from house '{house_id}'"}
