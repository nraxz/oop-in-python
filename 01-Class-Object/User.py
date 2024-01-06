class User:
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email

    def display_info(self):
        print(f"User ID: {self.user_id}, Username: {self.username}, Email: {self.email}")

    # Create a User object
    user1 = User(123, "johndoe", "johndoe@example.com")

    # Call the display_info method to print the user's information
    user1.display_info()  # Output: User ID: 123, Username: johndoe, Email: johndoe@example.com