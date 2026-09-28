import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from course import Course
from enrollment import Enrollment
from mentor import Mentor
from student import Student
from user import User


def test_student_inherits_from_user():
    student = Student(
        "Test Student",
        "student@example.com",
        "S001",
    )

    assert isinstance(student, User)
    assert student.name == "Test Student"
    assert student.email == "student@example.com"


def test_mentor_inherits_from_user():
    mentor = Mentor(
        "Test Mentor",
        "mentor@example.com",
        "M001",
        "Python",
    )

    assert isinstance(mentor, User)
    assert mentor.expertise == "Python"


def test_course_creation():
    mentor = Mentor(
        "Test Mentor",
        "mentor@example.com",
        "M001",
        "Python",
    )

    course = Course(
        "C001",
        "Python OOP",
        mentor,
        capacity=2,
    )

    assert course.course_id == "C001"
    assert course.name == "Python OOP"
    assert course.capacity == 2
    assert course.available_seats() == 2


def test_student_enrollment():
    student = Student(
        "Test Student",
        "student@example.com",
        "S001",
    )

    mentor = Mentor(
        "Test Mentor",
        "mentor@example.com",
        "M001",
        "Python",
    )

    course = Course(
        "C001",
        "Python OOP",
        mentor,
        capacity=2,
    )

    enrollment = Enrollment(student, course)

    assert enrollment.status == "Active"
    assert student.enrolled_courses == [course]
    assert course.students == [student]
    assert course.available_seats() == 1


def test_cancel_enrollment():
    student = Student(
        "Test Student",
        "student@example.com",
        "S001",
    )

    mentor = Mentor(
        "Test Mentor",
        "mentor@example.com",
        "M001",
        "Python",
    )

    course = Course(
        "C001",
        "Python OOP",
        mentor,
        capacity=2,
    )

    enrollment = Enrollment(student, course)
    enrollment.cancel()

    assert enrollment.status == "Cancelled"


def test_email_validation():
    assert User.validate_email("test@example.com") is True
    assert User.validate_email("invalid-email") is False