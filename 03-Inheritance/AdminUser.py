class AdminUser(User):
    def __init__(self, user_id, username, email, password, role):
        super().__init__(user_id, username, email, password)
        self._role = role

    def promote_to_admin(self):
        print(f"User {self._username} promoted to admin.")

    # Overriding the display_info method for AdminUser
    def display_info(self):
        print(f"Admin User - User ID: {self._user_id}, Username: {self._username}, Email: {self._email}, Role: {self._role}")

    # Create a regular user
    regular_user = User(1, "JohnDoe", "john.doe@email.com", "secret_password")

    # Create an admin user
    admin_user = AdminUser(2, "AdminJohn", "admin.john@email.com", "admin_password", "Administrator")

    # Display user information
    regular_user.display_info()  
    # Output: User ID: 1, Username: JohnDoe, Email: john.doe@email.com
    admin_user.display_info()    
    # Output: Admin User - User ID: 2, Username: AdminJohn, Email: admin.john@email.com, Role: Administrator

    # Promote the admin user
    admin_user.promote_to_admin()  
    # Output: User AdminJohn promoted to admin.
