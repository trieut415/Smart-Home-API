# room_api.py

class RoomAPI:
    def __init__(self):
        # Nested dictionary: { house_id: { floor_number: { room_name: room_data } } }
        self.rooms = {}

    def create_room(self, house_id, floor_number, room_name, **metadata):
        # Ensure house entry exists
        if house_id not in self.rooms:
            self.rooms[house_id] = {}
        # Ensure floor entry exists for the house
        if floor_number not in self.rooms[house_id]:
            self.rooms[house_id][floor_number] = {}
        # Check if room already exists
        if room_name in self.rooms[house_id][floor_number]:
            raise ValueError(f"Room '{room_name}' already exists on floor '{floor_number}' in house '{house_id}'.")
        
        room = {
            "house_id": house_id,
            "floor_number": floor_number,
            "room_name": room_name,
            "metadata": metadata
        }
        self.rooms[house_id][floor_number][room_name] = room
        print(f"Created room: {room}")
        return room
    
    def delete_room(self, house_id, floor_number, room_name):
        try:
            del self.rooms[house_id][floor_number][room_name]
            print(f"Deleted room '{room_name}' from floor '{floor_number}' in house '{house_id}'")
            return True
        except KeyError:
            raise ValueError(f"Room '{room_name}' on floor '{floor_number}' in house '{house_id}' does not exist.")
    
    def read_room(self, house_id, floor_number, room_name):
        try:
            room = self.rooms[house_id][floor_number][room_name]
            print(f"Reading room: {room}")
            return room
        except KeyError:
            raise ValueError(f"Room '{room_name}' on floor '{floor_number}' in house '{house_id}' not found.")
    
    def update_room(self, house_id, floor_number, room_name, **metadata):
        try:
            room = self.rooms[house_id][floor_number][room_name]
            # Merge existing metadata with new metadata
            room["metadata"].update(metadata)
            print(f"Updated room: {room}")
            return {"house_id": house_id, "floor_number": floor_number, "room_name": room_name, "updated_metadata": room["metadata"]}
        except KeyError:
            raise ValueError(f"Room '{room_name}' on floor '{floor_number}' in house '{house_id}' not found.")
