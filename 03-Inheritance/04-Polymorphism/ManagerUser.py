class ManagerUser(User):
    def __init__(self, user_id, username, email, password, role):
        super().__init__(user_id, username, email, password)
        self._auditions = []  # List to store auditions created by this manager

    def promote_to_manager(self):
        print(f"User {self._username} promoted to manager.")
        
    def create_audition(self, audition_name, description, deadline):
        new_audition = Audition(audition_name, description, deadline, manager=self)
        self._auditions.append(new_audition)
        print(f"Audition '{audition_name}' created successfully.")
        return new_audition

    def get_auditions(self):
        return self._auditions

    # Additional methods for audition management:
    def get_applications(self, audition):
        # Retrieve applications for the specified audition
        return audition.get_applications()  # Assuming Audition class has a method to access applications

    def review_application(self, application):
        # Implement logic for reviewing an application
        pass

    def approve_application(self, application):
        # Implement logic for approving an application
        pass

    def reject_application(self, application):
        # Implement logic for rejecting an application
        pass

    def display_info(self):
        print(f"Manager User - User ID: {self._user_id}, Username: {self._username}, Email: {self._email}")