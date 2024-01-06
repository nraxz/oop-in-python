class User:
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email

    def display_info(self):
        print(f"User ID: {self.user_id}, Username: {self.username}, Email: {self.email}")

class AdminUser(User):
    def __init__(self, user_id, username, email, role):
        super().__init__(user_id, username, email)
        self.role = role

    # Overriding the display_info method for AdminUser
    def display_info(self):
        print(f"Admin User - User ID: {self.user_id}, Username: {self.username}, Email: {self.email}, Role: {self.role}")

class ManagerUser(User):
    def __init__(self, user_id, username, email, team):
        super().__init__(user_id, username, email)
        self.team = team

    # Overriding the display_info method for ManagerUser
    def display_info(self):
        print(f"Manager User - User ID: {self.user_id}, Username: {self.username}, Email: {self.email}, Team: {self.team}")
