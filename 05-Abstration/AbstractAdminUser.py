from abc import ABC, abstractmethod

class AbstractAdmin(ABC):
    def __init__(self, user_id, username, email, password, role):
        super().__init__(user_id, username, email, password)  # Call the constructor of the superclass (AbstractUser)
        self._role = role

    @abstractmethod
    def promote_to_admin(self, user):
        pass  # Concrete implementation in subclasses

    @abstractmethod
    def manage_users(self):
        pass  # Concrete implementation in subclasses   

    # Overriding the display_info method for AdminUser
    def display_info(self):
        print(f"Admin User - User ID: {self._user_id}, Username: {self._username}, Email: {self._email}, Role: {self._role}")
