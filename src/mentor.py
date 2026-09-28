from user import User


class Mentor(User):
    """Represents a mentor on the learning platform."""

    def __init__(self, name, email, user_id, expertise):
        super().__init__(name, email, user_id)
        self.expertise = expertise
        self.courses = []

    def add_course(self, course):
        """Add a course managed by the mentor."""
        self.courses.append(course)

    def display_info(self):
        """Display mentor information."""
        print("=== Mentor ===")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"User ID: {self.user_id}")
        print(f"Expertise: {self.expertise}")
        print(f"Courses: {len(self.courses)}")