from user import User


class Student(User):
    """Represents a student on the learning platform."""

    def __init__(self, name, email, user_id):
        super().__init__(name, email, user_id)
        self.enrolled_courses = []

    def enroll(self, course):
        """Add a course to the student's enrolled courses."""
        self.enrolled_courses.append(course)

    def display_info(self):
        """Display student information."""
        print("=== Student ===")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"User ID: {self.user_id}")
        print(f"Courses: {len(self.enrolled_courses)}")