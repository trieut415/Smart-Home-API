from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Dict, Optional, Any

router = APIRouter()

# In-memory storage for devices
devices = {}

# Pydantic Models
class DeviceCreate(BaseModel):
    device_id: str = Field(..., description="Unique identifier for the device")
    device_type: str = Field(..., description="Type of the device")
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DeviceResponse(BaseModel):
    device_id: str
    device_type: str
    metadata: Dict[str, Any]

@router.post("/", response_model=DeviceResponse)
def create_device(device: DeviceCreate):
    if device.device_id in devices:
        raise HTTPException(status_code=400, detail="Device with this ID already exists")
    
    new_device = {
        "device_id": device.device_id,
        "device_type": device.device_type,
        "metadata": device.metadata
    }
    devices[device.device_id] = new_device
    return new_device

@router.get("/{device_id}", response_model=DeviceResponse)
def read_device(device_id: str):
    device = devices.get(device_id)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    return device
