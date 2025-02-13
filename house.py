# house_api.py

class HouseAPI:
    def create_house(self, house_name, **metadata):
        print(f"Creating house '{house_name}' with metadata: {metadata}")
        # Stub: Add logic to create a house
        return {"house_name": house_name, "metadata": metadata}
    
    def delete_house(self, house_id):
        print(f"Deleting house with ID: {house_id}")
        # Stub: Add logic to delete a house
        return True
    
    def read_house(self, house_id):
        print(f"Reading house with ID: {house_id}")
        # Stub: Add logic to read house details
        return {"house_id": house_id, "name": "Example House", "metadata": {}}
    
    def update_house(self, house_id, **metadata):
        print(f"Updating house with ID: {house_id} with metadata: {metadata}")
        # Stub: Add logic to update house metadata
        return {"house_id": house_id, "updated_metadata": metadata}
    
    def add_floor(self, house_id, floor_number, **metadata):
        print(f"Adding floor '{floor_number}' to house with ID: {house_id} with metadata: {metadata}")
        # Stub: Add logic to add a floor
        return {"house_id": house_id, "floor_number": floor_number, "metadata": metadata}
    
    def delete_floor(self, house_id, floor_number):
        print(f"Deleting floor '{floor_number}' from house with ID: {house_id}")
        # Stub: Add logic to delete a floor
        return True