class Enrollment:
    """Represents a student's enrollment in a course."""

    enrollment_count = 0

    def __init__(self, student, course):
        self.student = student
        self.course = course
        self.status = "Active"

        course.add_student(student)
        student.enroll(course)

        Enrollment.enrollment_count += 1

    def cancel(self):
        """Cancel the enrollment."""
        self.status = "Cancelled"

    def display_info(self):
        """Display enrollment information."""
        print("=== Enrollment ===")
        print(f"Student: {self.student.name}")
        print(f"Course: {self.course.name}")
        print(f"Status: {self.status}")