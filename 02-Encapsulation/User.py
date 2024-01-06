class User:
    def __init__(self, user_id, username, email, password):
        self._user_id = user_id
        self._username = username
        self._email = email
        self._password = password  # Consider hashing for security
        self._is_authenticated = False

    def authenticate(self, entered_password):
        if entered_password == self._password:
            self._is_authenticated = True
            print("Authentication successful.")
            return True  # Explicitly return success status
        else:
            print("Authentication failed.")
            return False  # Explicitly return failure status

    def get_username(self):
        return self._username

    def get_email(self):
        return self._email

    def set_email(self, new_email):
        self._email = new_email
        print("Email updated successfully.")

    def get_id(self):
        return self._user_id

    def is_authenticated(self):
        return self._is_authenticated

    def display_info(self):
        print(f"User ID: {self.get_id()}, Username: {self.get_username()}, Email: {self.get_email()}")
