from course import Course
from enrollment import Enrollment
from mentor import Mentor
from student import Student
from user import User

def main():
    # Create users
    student = Student(
        "Nattarkani",
        "nattarkani@example.com",
        "S001",
    )

    mentor = Mentor(
        "Priya",
        "priya@example.com",
        "M001",
        "Python and AI",
    )

    # Create course
    course = Course(
        "C001",
        "Python OOP",
        mentor,
        capacity=30,
    )

    mentor.add_course(course)

    # Create enrollment
    enrollment = Enrollment(student, course)

    # Demonstrate polymorphism
    users = [student, mentor]

    print("=== Course Management System ===\n")

    for user in users:
        user.display_info()
        print()

    course.display_info()
    print()

    enrollment.display_info()
    print()

    # Demonstrate static method
    print(
        "Valid email:",
        User.validate_email(student.email)
    )

    # Demonstrate class method
    print(
        "Total users:",
        User.get_total_users()
    )


if __name__ == "__main__":
    main()