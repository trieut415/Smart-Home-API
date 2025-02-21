# device_api.py

class DeviceAPI:
    def __init__(self):
        # In-memory storage for devices
        self.devices = {}

    def create_device(self, device_id, device_type, **metadata):
        if device_id in self.devices:
            raise ValueError(f"Device with ID {device_id} already exists.")
        device = {
            "device_id": device_id,
            "device_type": device_type,
            "metadata": metadata,
            "data": {"temperature": None, "humidity": None},  # Placeholder for sensor data
            "assigned_to": None,
        }
        self.devices[device_id] = device
        print(f"Created device: {device}")
        return device
    
    def delete_device(self, device_id):
        if device_id not in self.devices:
            raise ValueError(f"Device with ID {device_id} not found.")
        del self.devices[device_id]
        print(f"Deleted device with ID: {device_id}")
        return True
    
    def read_device(self, device_id):
        device = self.devices.get(device_id)
        if not device:
            raise ValueError(f"Device with ID {device_id} not found.")
        print(f"Reading device data: {device}")
        return {"device_id": device_id, "data": device.get("data", {})}
    
    def update_device(self, device_id, **metadata):
        device = self.devices.get(device_id)
        if not device:
            raise ValueError(f"Device with ID {device_id} not found.")
        # Update metadata by merging existing with new values
        device["metadata"].update(metadata)
        print(f"Updated device: {device}")
        return {"device_id": device_id, "updated_metadata": device["metadata"]}
    
    def assign_device(self, device_id, location_type, location_identifier):
        device = self.devices.get(device_id)
        if not device:
            raise ValueError(f"Device with ID {device_id} not found.")
        assignment = {location_type: location_identifier}
        device["assigned_to"] = assignment
        print(f"Assigned device '{device_id}' to {location_type} '{location_identifier}'")
        return {"device_id": device_id, "assigned_to": assignment}
