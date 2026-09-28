class Course:
    """Represents a course offered on the learning platform."""

    def __init__(self, course_id, name, mentor, capacity=30):
        self.course_id = course_id
        self.name = name
        self.mentor = mentor
        self.__capacity = capacity
        self.__students = []

    @property
    def capacity(self):
        """Return the course capacity."""
        return self.__capacity

    @property
    def students(self):
        """Return the enrolled students."""
        return self.__students.copy()

    def add_student(self, student):
        """Add a student to the course."""
        if len(self.__students) >= self.__capacity:
            raise ValueError("Course capacity is full.")

        if student in self.__students:
            raise ValueError("Student is already enrolled.")

        self.__students.append(student)

    def available_seats(self):
        """Return the number of available seats."""
        return self.__capacity - len(self.__students)

    def display_info(self):
        """Display course information."""
        print("=== Course ===")
        print(f"Course ID: {self.course_id}")
        print(f"Course Name: {self.name}")
        print(f"Mentor: {self.mentor.name}")
        print(f"Capacity: {self.__capacity}")
        print(f"Enrolled Students: {len(self.__students)}")
        print(f"Available Seats: {self.available_seats()}")