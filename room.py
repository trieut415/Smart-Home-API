# room_api.py

class RoomAPI:
    def create_room(self, house_id, floor_number, room_name, **metadata):
        print(f"Creating room '{room_name}' on floor '{floor_number}' in house ID {house_id} with metadata: {metadata}")
        # Stub: Add logic to create a room
        return {"house_id": house_id, "floor_number": floor_number, "room_name": room_name, "metadata": metadata}
    
    def delete_room(self, house_id, floor_number, room_name):
        print(f"Deleting room '{room_name}' from floor '{floor_number}' in house ID {house_id}")
        # Stub: Add logic to delete a room
        return True
    
    def read_room(self, house_id, floor_number, room_name):
        print(f"Reading room '{room_name}' on floor '{floor_number}' in house ID {house_id}")
        # Stub: Add logic to read room details
        return {"house_id": house_id, "floor_number": floor_number, "room_name": room_name, "metadata": {}}
    
    def update_room(self, house_id, floor_number, room_name, **metadata):
        print(f"Updating room '{room_name}' on floor '{floor_number}' in house ID {house_id} with metadata: {metadata}")
        # Stub: Add logic to update room metadata
        return {"house_id": house_id, "floor_number": floor_number, "room_name": room_name, "updated_metadata": metadata}