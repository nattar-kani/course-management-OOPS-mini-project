from abc import ABC, abstractmethod


class User(ABC):
    """Abstract base class for all platform users."""

    total_users = 0

    def __init__(self, name, email, user_id):
        self.name = name
        self.__email = email
        self.user_id = user_id
        User.total_users += 1

    @property
    def email(self):
        """Return the user's email."""
        return self.__email

    @email.setter
    def email(self, value):
        """Update the user's email after validation."""
        if not self.validate_email(value):
            raise ValueError("Invalid email address")
        self.__email = value

    @staticmethod
    def validate_email(email):
        """Validate an email address."""
        return "@" in email and "." in email

    @classmethod
    def get_total_users(cls):
        """Return the total number of users created."""
        return cls.total_users

    @abstractmethod
    def display_info(self):
        """Display user information."""
        pass