class AdminUser(User):
    def __init__(self, user_id, username, email, password, role):
        super().__init__(user_id, username, email, password)
        self._role = role

    def promote_to_admin(self):
        print(f"User {self._username} promoted to admin.")

    # Overriding the display_info method for AdminUser
    def display_info(self):
        print(f"Admin User - User ID: {self._user_id}, Username: {self._username}, Email: {self._email}, Role: {self._role}")