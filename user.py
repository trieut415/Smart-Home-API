# user_api.py

class UserAPI:
    def __init__(self):
        # In-memory storage for users and a counter for unique user IDs.
        self.users = {}
        self.next_user_id = 1

    def create_user(self, username, **attributes):
        user_id = self.next_user_id
        self.next_user_id += 1
        user = {
            "user_id": user_id,
            "username": username,
            "attributes": attributes
        }
        self.users[user_id] = user
        print(f"Created user: {user}")
        return user
    
    def delete_user(self, user_id):
        if user_id not in self.users:
            raise ValueError(f"User with ID {user_id} not found.")
        del self.users[user_id]
        print(f"Deleted user with ID: {user_id}")
        return True
    
    def read_user(self, user_id):
        user = self.users.get(user_id)
        if not user:
            raise ValueError(f"User with ID {user_id} not found.")
        print(f"Reading user: {user}")
        return user
    
    def update_user(self, user_id, **attributes):
        user = self.users.get(user_id)
        if not user:
            raise ValueError(f"User with ID {user_id} not found.")
        # Update attributes by merging existing with new values
        user["attributes"].update(attributes)
        print(f"Updated user: {user}")
        return {"user_id": user_id, "updated_attributes": user["attributes"]}


# Example usage:
if __name__ == "__main__":
    api = UserAPI()
    # Create a new user; user_id is auto-generated.
    user = api.create_user("john_doe", email="john@example.com")
    # Read user details.
    print(api.read_user(user["user_id"]))
    # Update user attributes.
    print(api.update_user(user["user_id"], email="john_new@example.com"))
    # Delete the user.
    api.delete_user(user["user_id"])
