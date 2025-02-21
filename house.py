# house_api.py

class HouseAPI:
    def __init__(self):
        # In-memory storage for houses
        self.houses = {}
    
    def create_house(self, house_name, **metadata):
        # Using house name as a unique identifier for simplicity
        if house_name in self.houses:
            raise ValueError(f"House '{house_name}' already exists.")
        house = {
            "house_name": house_name,
            "metadata": metadata,
            "floors": {}  # Floor info will be stored here
        }
        self.houses[house_name] = house
        print(f"Created house: {house}")
        return house
    
    def delete_house(self, house_id):
        # Here, house_id is actually the house_name
        if house_id not in self.houses:
            raise ValueError(f"House '{house_id}' not found.")
        del self.houses[house_id]
        print(f"Deleted house with ID: {house_id}")
        return True
    
    def read_house(self, house_id):
        house = self.houses.get(house_id)
        if not house:
            raise ValueError(f"House '{house_id}' not found.")
        print(f"Reading house: {house}")
        return house
    
    def update_house(self, house_id, **metadata):
        house = self.houses.get(house_id)
        if not house:
            raise ValueError(f"House '{house_id}' not found.")
        # Merge new metadata into the existing metadata
        house["metadata"].update(metadata)
        print(f"Updated house: {house}")
        return {"house_id": house_id, "updated_metadata": house["metadata"]}
    
    def add_floor(self, house_id, floor_number, **metadata):
        house = self.houses.get(house_id)
        if not house:
            raise ValueError(f"House '{house_id}' not found.")
        if floor_number in house["floors"]:
            raise ValueError(f"Floor '{floor_number}' already exists in house '{house_id}'.")
        floor = {"floor_number": floor_number, "metadata": metadata, "rooms": {}}
        house["floors"][floor_number] = floor
        print(f"Added floor: {floor} to house '{house_id}'")
        return {"house_id": house_id, "floor_number": floor_number, "metadata": metadata}
    
    def delete_floor(self, house_id, floor_number):
        house = self.houses.get(house_id)
        if not house:
            raise ValueError(f"House '{house_id}' not found.")
        if floor_number not in house["floors"]:
            raise ValueError(f"Floor '{floor_number}' not found in house '{house_id}'.")
        del house["floors"][floor_number]
        print(f"Deleted floor '{floor_number}' from house '{house_id}'")
        return True
