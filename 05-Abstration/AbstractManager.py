from abc import ABC, abstractmethod

class AbstractManager(ABC):
    def __init__(self, user_id, username, email, password):
        super().__init__()  # Call the constructor of the superclass (User)
        self._user_id = user_id
        self._username = username
        self._email = email
        self._password = password
        self._auditions = []  # List to store auditions

    @abstractmethod
    def create_audition(self, audition_name, description, deadline):
        pass  # Abstract method, implementation will be provided in subclasses

    @abstractmethod
    def get_auditions(self):
        pass  # Abstract method, implementation will be provided in subclasses

    # Additional abstract methods for audition management:
    @abstractmethod
    def get_applications(self, audition):
        pass

    @abstractmethod
    def review_application(self, application):
        pass

    @abstractmethod
    def approve_application(self, application):
        pass

    @abstractmethod
    def reject_application(self, application):
        pass

    def display_info(self):
        print(f"Manager User - User ID: {self._user_id}, Username: {self._username}, Email: {self._email}")
