from abc import ABC, abstractmethod

class AbstractUser(ABC):
    def __init__(self, user_id, username, email, password):
        self._user_id = user_id
        self._username = username
        self._email = email
        self._password = password
        self._is_authenticated = False

    @abstractmethod
    def authenticate(self, entered_password):
        pass  # Abstract method, concrete implementation in subclasses

    @abstractmethod
    def get_username(self):
        pass

    @abstractmethod
    def get_email(self):
        pass

    @abstractmethod
    def set_email(self, new_email):
        pass

    @abstractmethod
    def get_id(self):
        pass

    @abstractmethod
    def is_authenticated(self):
        pass

    def display_info(self):
        print(f"User ID: {self._user_id}, Username: {self._username}, Email: {self._email}")
