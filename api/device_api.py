from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Dict, Optional, Any

router = APIRouter()

# In-memory storage for devices
devices = {}

class DeviceCreate(BaseModel):
    device_id: str = Field(..., description="Unique identifier for the device")
    device_type: str = Field(..., description="Type of the device")
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DeviceResponse(BaseModel):
    device_id: str
    device_type: str
    metadata: Dict[str, Any]
    assigned_to: Optional[Dict[str, str]] = None  # Ensure 'assigned_to' is part of the response model

# POST: Create Device
@router.post("/", response_model=DeviceResponse)
def create_device(device: DeviceCreate):
    if device.device_id in devices:
        raise HTTPException(status_code=400, detail="Device with this ID already exists")

    devices[device.device_id] = {
        "device_id": device.device_id,
        "device_type": device.device_type,
        "metadata": device.metadata,
        "assigned_to": None  # Explicitly set 'assigned_to' as None initially
    }
    return devices[device.device_id]

# PUT: Update Device Metadata
@router.put("/{device_id}", response_model=DeviceResponse)
def update_device(device_id: str, update_data: Dict[str, Any]):
    if device_id not in devices:
        raise HTTPException(status_code=404, detail="Device not found")

    if "metadata" in update_data:
        devices[device_id]["metadata"].update(update_data["metadata"])

    return devices[device_id]

# POST: Assign Device to a Location
class DeviceAssignment(BaseModel):
    location_type: str
    location_identifier: str

@router.post("/{device_id}/assign", response_model=DeviceResponse)
def assign_device(device_id: str, assignment: DeviceAssignment):
    if device_id not in devices:
        raise HTTPException(status_code=404, detail="Device not found")

    devices[device_id]["assigned_to"] = {
        assignment.location_type: assignment.location_identifier
    }

    return devices[device_id]

# DELETE: Remove Device
@router.delete("/{device_id}")
def delete_device(device_id: str):
    if device_id not in devices:
        raise HTTPException(status_code=404, detail="Device not found")

    del devices[device_id]
    return {"message": f"Device {device_id} deleted successfully"}

@router.get("/{device_id}", response_model=DeviceResponse)
def read_device(device_id: str):
    if device_id not in devices:
        raise HTTPException(status_code=404, detail="Device not found")
    return devices[device_id]
