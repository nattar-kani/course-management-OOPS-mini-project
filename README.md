# Course Management System using Python OOP

A Python-based Course Management System built to demonstrate core Object-Oriented Programming concepts along with a practical Git/GitHub development workflow.

The system manages users, students, mentors, courses, and enrollments.

## Features

* Create and manage users
* Create Student and Mentor roles
* Create courses
* Assign mentors to courses
* Enroll students in courses
* Track available course seats
* Cancel enrollments
* Display user, course, and enrollment information
* Validate email addresses
* Track total users
* Unit testing with `pytest`

## OOP Concepts Demonstrated

### 1. Abstraction

`User` is implemented as an abstract base class using Python's `ABC` and `abstractmethod`.

```python
class User(ABC):
```

The `display_info()` method is defined as an abstract method.

### 2. Inheritance

`Student` and `Mentor` inherit from the `User` class.

```python
class Student(User):
```

```python
class Mentor(User):
```

Common user properties are maintained in the parent class while role-specific functionality is implemented in the child classes.

### 3. Encapsulation

Private attributes are used to protect internal data.

For example, `Course` stores capacity and enrolled students using private attributes:

```python
self.__capacity
self.__students
```

Access is controlled through properties and methods.

### 4. Polymorphism

`Student` and `Mentor` both override the `display_info()` method inherited from `User`.

The same method call can therefore produce different behavior depending on the object.

```python
users = [student, mentor]

for user in users:
    user.display_info()
```

### 5. Instance Methods

The project uses instance methods such as:

```text
enroll()
add_course()
add_student()
available_seats()
cancel()
display_info()
```

These methods operate on individual objects.

### 6. Static Method

Email validation is implemented using `@staticmethod`.

```python
User.validate_email("test@example.com")
```

The method does not depend on a particular User object.

### 7. Class Method

The `User` class uses a class variable to track the number of users and a class method to retrieve it.

```python
User.get_total_users()
```

## Class Architecture

```text
                         User (Abstract)
                         /             \
                        /               \
                   Student             Mentor
                      |                   |
                      |                   |
                      +---- Enrollment ---+
                               |
                               |
                            Course
```

### Classes

| Class        | Responsibility                          |
| ------------ | --------------------------------------- |
| `User`       | Common user properties and behavior     |
| `Student`    | Student-specific functionality          |
| `Mentor`     | Mentor-specific functionality           |
| `Course`     | Course information and student capacity |
| `Enrollment` | Manages student-course enrollment       |

## Project Structure

```text
course-management-system/
│
├── src/
│   ├── user.py
│   ├── student.py
│   ├── mentor.py
│   ├── course.py
│   ├── enrollment.py
│   └── main.py
│
├── tests/
│   └── test_course_management.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/course-management-system.git
cd course-management-system
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Running the Application

Run the main application from the project root:

```bash
python src\main.py
```

## Running Tests

Run the test suite using:

```bash
python -m pytest
```

Expected result:

```text
6 passed
```

## Example Usage

The application creates a student and mentor, creates a Python OOP course, and enrolls the student.

Example:

```python
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

course = Course(
    "C001",
    "Python OOP",
    mentor,
    capacity=30,
)

enrollment = Enrollment(student, course)
```

The enrollment automatically connects the student with the course.

## Example Output

```text
=== Course Management System ===

=== Student ===
Name: Nattarkani
Email: nattarkani@example.com
User ID: S001
Courses: 1

=== Mentor ===
Name: Priya
Email: priya@example.com
User ID: M001
Expertise: Python and AI
Courses: 1

=== Course ===
Course ID: C001
Course Name: Python OOP
Mentor: Priya
Capacity: 30
Enrolled Students: 1
Available Seats: 29

=== Enrollment ===
Student: Nattarkani
Course: Python OOP
Status: Active

Valid email: True
Total users: 2
```

## Git and GitHub Workflow

The project is developed using feature branches and meaningful commits.

Example workflow:

```bash
git switch -c feature/user-model
git add .
git commit -m "Add abstract User class"

git switch main
git merge feature/user-model
```

Additional features are developed in separate branches and merged into `main`.

The project also uses GitHub Pull Requests for feature integration.

## Development Workflow

```text
main
 │
 ├── feature/user-model
 │
 ├── feature/user-roles
 │
 └── feature/course-enrollment
```

Each feature branch contains a focused change and meaningful commit messages.

## Testing

The test suite verifies:

* User inheritance
* Student inheritance
* Mentor inheritance
* Course creation
* Student enrollment
* Enrollment cancellation
* Email validation

