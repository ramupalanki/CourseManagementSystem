# Course Management System

A production-style Python OOP mini-project that demonstrates core Object-Oriented Programming concepts while using a professional Git/GitHub workflow.

---

## 1. Project Information

**Project Name:** Course Management System  
**Language:** Python  
**Python Version:** 3.10+  
**Repository:** `course-management-system`

> **Before submission:** Update the GitHub repository URL and Pull Request URL in the **Submission Details** section at the bottom of this README.

---

# 2. Problem Statement

Build a **Course Management System** using Python Object-Oriented Programming.

The system should allow:

- Students to register in the system.
- Mentors to manage courses.
- Mentors to be assigned to courses.
- Students to enroll in courses.
- Student course progress to be tracked.
- Enrollment status to be displayed.
- User and course IDs to be generated automatically.

The project must demonstrate the following Python OOP concepts:

- Inheritance
- Encapsulation
- Polymorphism
- Abstraction
- Instance methods
- `@staticmethod`
- `@classmethod`

The project must also demonstrate professional software development practices using:

- Git
- Feature branches
- Meaningful commits
- Merging
- Pull Requests
- GitHub
- Unit testing
- Professional documentation

---

# 3. Architecture

```text
                    User (Abstract Class)
                           │
                ┌──────────┴──────────┐
                │                     │
             Student                Mentor
                │                     │
                │                     │
                └────── Enrollment ───┘
                           │
                         Course
```

## Project Structure

```text
course-management-system/
│
├── course_management_system/
│   ├── __init__.py
│   └── models.py
│
├── tests/
│   └── test_models.py
│
├── main.py
├── requirements.txt
├── .gitignore
├── PROJECT_STRUCTURE.txt
└── README.md
```

---

# 4. Classes

## User

`User` is the abstract base class for all users.

Responsibilities:

- Generate user IDs.
- Store name and email.
- Validate email addresses.
- Provide common user functionality.
- Define the abstract `get_role()` method.

```python
class User(ABC):
    @abstractmethod
    def get_role(self):
        raise NotImplementedError
```

---

## Student

`Student` inherits from `User`.

Responsibilities:

- Store student information.
- Maintain student enrollments.
- Display course progress.

```python
class Student(User):
    ...
```

---

## Mentor

`Mentor` inherits from `User`.

Responsibilities:

- Store mentor expertise.
- Manage assigned courses.
- Assign courses to the mentor.

```python
class Mentor(User):
    ...
```

---

## Course

`Course` represents a course offered by the system.

Responsibilities:

- Generate course IDs.
- Store course title.
- Store course duration.
- Maintain assigned mentor.

---

## Enrollment

`Enrollment` connects a Student and a Course.

Responsibilities:

- Store student and course.
- Track progress.
- Validate progress.
- Display enrollment status.

Possible statuses:

```text
Not Started
In Progress
Completed
```

---

## Report

`Report` provides reusable reporting functionality.

It demonstrates polymorphism by working with different `User` objects through their common interface.

---

# 5. OOP Concepts Demonstrated

## 5.1 Inheritance

`Student` and `Mentor` inherit from `User`.

```python
class Student(User):
    pass

class Mentor(User):
    pass
```

This allows common functionality to be reused.

---

## 5.2 Abstraction

`User` is implemented as an abstract base class.

```python
from abc import ABC, abstractmethod

class User(ABC):

    @abstractmethod
    def get_role(self):
        raise NotImplementedError
```

Every child class must implement `get_role()`.

---

## 5.3 Encapsulation

Private attributes are used to protect internal data.

Example:

```python
self.__enrollments = []
self.__progress = 0
```

Progress cannot be changed directly.

Instead:

```python
enrollment.update_progress(75)
```

The method validates the value before updating it.

---

## 5.4 Polymorphism

Both `Student` and `Mentor` implement the same method differently.

```python
student.get_role()
```

returns:

```text
Student
```

while:

```python
mentor.get_role()
```

returns:

```text
Mentor
```

The same method name behaves differently depending on the object.

---

## 5.5 Instance Methods

Instance methods operate on individual objects.

Examples:

```python
student.get_progress()

mentor.assign_course(course)

enrollment.update_progress(75)

course.course_summary()
```

---

## 5.6 Static Method

The email validation method does not depend on a particular object.

```python
User.validate_email("student@example.com")
```

Implementation:

```python
@staticmethod
def validate_email(email):
    return "@" in email and "." in email.split("@")[-1]
```

---

## 5.7 Class Method

Class methods are used for automatic ID generation.

```python
@classmethod
def _generate_id(cls):
    ...
```

The class maintains the ID sequence.

---

# 6. Features

The application provides the following features:

- User management
- Student creation
- Mentor creation
- Course creation
- Mentor-course assignment
- Student enrollment
- Course progress tracking
- Enrollment status
- Email validation
- Automatic user IDs
- Automatic course IDs
- Console reports
- Unit tests
- Object-oriented architecture
- Git/GitHub workflow
- Professional README documentation

---

# 7. Requirements

The project requires:

- Python 3.10 or later
- Git
- GitHub account

No external Python packages are required.

---

# 8. Installation

## Step 1: Clone the Repository

Clone the GitHub repository using the repository URL from the **Submission Details** section below.

```bash
git clone <YOUR_REPOSITORY_URL>
```

Example:

```bash
git clone https://github.com/your-github-username/course-management-system.git
```

> Replace the example URL with your actual repository URL.

Navigate into the project:

```bash
cd course-management-system
```

---

# 9. Create Virtual Environment

On Windows:

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

On Linux/macOS:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

---

# 10. Install Dependencies

Run:

```bash
pip install -r requirements.txt
```

The project currently uses only the Python standard library, so no third-party dependencies are required.

---

# 11. Run the Application

Execute:

```bash
python main.py
```

Expected output:

```text
=== COURSE MANAGEMENT SYSTEM ===

--- Users ---
[1000] Anita Rao <anita@example.com> - Mentor
[1001] Ravi Kumar <ravi@example.com> - Student
[1002] Priya Sharma <priya@example.com> - Student

--- Courses ---
Course #1: Python OOP Masterclass | 30 hours | Mentor: Anita Rao
Course #2: AI Fundamentals | 24 hours | Mentor: Anita Rao

--- Enrollments ---
Ravi Kumar -> Python OOP Masterclass | 75% | In Progress
Priya Sharma -> Python OOP Masterclass | 100% | Completed
Ravi Kumar -> AI Fundamentals | 25% | In Progress

--- Student Progress ---
Python OOP Masterclass: 75%
AI Fundamentals: 25%

--- OOP Demonstration ---
Student role: Student
Mentor role: Mentor
Valid email? True
```

---

# 12. Run Unit Tests

Run:

```bash
python -m unittest discover -s tests -v
```

Expected result:

```text
Ran 6 tests

OK
```

The tests cover:

- Inheritance
- Static method
- Class method ID generation
- Encapsulation
- Progress validation
- Course assignment

---

# 13. Important Code Examples

## Creating a Mentor

```python
mentor = Mentor(
    "Anita Rao",
    "anita@example.com",
    "Python & AI"
)
```

---

## Creating a Student

```python
student = Student(
    "Ravi Kumar",
    "ravi@example.com"
)
```

---

## Creating a Course

```python
course = Course(
    "Python OOP Masterclass",
    30
)
```

---

## Assigning Mentor

```python
mentor.assign_course(course)
```

---

## Enrolling a Student

```python
enrollment = Enrollment(
    student,
    course
)
```

---

## Updating Progress

```python
enrollment.update_progress(75)
```

The system automatically determines the status:

```text
0%       → Not Started
1-99%    → In Progress
100%     → Completed
```

---

# 14. Git/GitHub Workflow

The project follows a feature-branch-based Git workflow.

```text
main
 │
 ├── feature/user-course-models
 │          │
 │          └── Pull Request
 │                    │
 └─────────── Merge ──┘
 │
 ├── feature/enrollment-progress
 │          │
 │          └── Pull Request
 │                    │
 └─────────── Merge ──┘
 │
 └── feature/tests-readme
            │
            └── Pull Request
                      │
              ────────┘
```

---

# 15. Git Commands

## Initialize Repository

```bash
git init
git branch -M main
```

Add files:

```bash
git add .
```

Initial commit:

```bash
git commit -m "chore: initialize course management project"
```

---

# 16. Create GitHub Repository

Create a **public GitHub repository** named:

```text
course-management-system
```

Connect the local project:

```bash
git remote add origin <YOUR_REPOSITORY_URL>
```

Push:

```bash
git push -u origin main
```

---

# 17. Feature Branch

Create the first feature branch:

```bash
git checkout -b feature/user-course-models
```

Implement the User, Student, Mentor and Course classes.

Commit:

```bash
git add .
git commit -m "feat: add user student mentor and course models"
```

Push:

```bash
git push -u origin feature/user-course-models
```

---

# 18. Pull Request

Open GitHub and:

1. Open the repository.
2. Select **Pull requests**.
3. Select **New Pull Request**.
4. Base branch: `main`.
5. Compare branch: `feature/user-course-models`.
6. Add a meaningful title.
7. Describe the changes.
8. Create the Pull Request.
9. Review the changes.
10. Merge the Pull Request.

---

# 19. Enrollment Feature Branch

After merging:

```bash
git checkout main
git pull origin main
```

Create another feature branch:

```bash
git checkout -b feature/enrollment-progress
```

Implement enrollment and progress tracking.

Commit:

```bash
git add .
git commit -m "feat: add enrollment and progress tracking"
```

Push:

```bash
git push -u origin feature/enrollment-progress
```

Create another Pull Request and merge it into `main`.

---

# 20. Tests and Documentation Branch

Create the final feature branch:

```bash
git checkout main
git pull origin main
git checkout -b feature/tests-readme
```

Add tests:

```bash
git add tests/
git commit -m "test: add course management unit tests"
```

Update documentation:

```bash
git add README.md
git commit -m "docs: add project architecture and usage guide"
```

Push:

```bash
git push -u origin feature/tests-readme
```

Create and merge the Pull Request.

---

# 21. Meaningful Commit History

A professional commit history should look similar to:

```text
docs: add project architecture and usage guide
test: add course management unit tests
feat: add enrollment and progress tracking
feat: add user student mentor and course models
chore: initialize course management project
```

View the history:

```bash
git log --oneline --graph --decorate --all
```

---

# 22. Merge Conflict Demonstration

The project can also demonstrate Git conflict resolution.

Create the first branch:

```bash
git checkout main
git checkout -b feature/report-a
```

Modify the same line in `main.py`.

Commit:

```bash
git add main.py
git commit -m "feat: update application heading"
```

Return to main:

```bash
git checkout main
```

Create another branch:

```bash
git checkout -b feature/report-b
```

Modify the **same line** differently.

Commit:

```bash
git add main.py
git commit -m "feat: customize application heading"
```

Return to main:

```bash
git checkout main
```

Merge the first branch:

```bash
git merge feature/report-a
```

Now merge the second:

```bash
git merge feature/report-b
```

Git should report a merge conflict.

The file will contain conflict markers:

```text
<<<<<<< HEAD
Current version
=======
Incoming version
>>>>>>> feature/report-b
```

Resolve the conflict manually.

Remove the conflict markers and keep the required code.

Then:

```bash
git add main.py
git commit -m "fix: resolve merge conflict in application heading"
```

Push the final history:

```bash
git push origin main
```

---

# 23. Production-Ready Checklist

Before submitting the project, verify:

- [x] Python OOP architecture implemented
- [x] Inheritance implemented
- [x] Encapsulation implemented
- [x] Polymorphism implemented
- [x] Abstraction implemented
- [x] Instance methods implemented
- [x] `@staticmethod` implemented
- [x] `@classmethod` implemented
- [x] Student functionality implemented
- [x] Mentor functionality implemented
- [x] Course functionality implemented
- [x] Enrollment functionality implemented
- [x] Progress tracking implemented
- [x] Unit tests included
- [x] README included
- [x] `.gitignore` included
- [x] Feature branches used
- [x] Meaningful commits used
- [x] Pull Request created
- [x] Pull Request merged
- [ ] GitHub repository made public
- [ ] Final repository URL added below
- [ ] Final Pull Request URL added below

---

# 24. Submission Details

## GitHub Repository

Add the actual repository URL here after creating the GitHub repository.

```text
Repository URL:
https://github.com/YOUR_GITHUB_USERNAME/course-management-system
```

## Pull Request

Add the actual Pull Request URL here after creating the PR.

```text
Pull Request URL:
https://github.com/YOUR_GITHUB_USERNAME/course-management-system/pull/1
```

---

# 25. Final Project Explanation

The Course Management System is designed using Python Object-Oriented Programming.

The abstract `User` class provides common functionality for all users. `Student` and `Mentor` inherit from `User`, demonstrating inheritance.

The `User` class defines the abstract `get_role()` method, demonstrating abstraction. Both child classes implement this method differently, demonstrating polymorphism.

Private attributes such as `__enrollments`, `__progress`, and `__mentor` demonstrate encapsulation. Access to these attributes is controlled through methods and properties.

The project also demonstrates different types of methods:

- Instance methods for object-specific behavior.
- `@staticmethod` for email validation.
- `@classmethod` for automatic ID generation.

The `Enrollment` class connects students and courses and provides controlled progress tracking.

Git is used to manage development through feature branches and meaningful commits. Pull Requests provide a formal review and merge process before changes reach the `main` branch.

The final project therefore demonstrates both **Python OOP concepts** and a practical **Git/GitHub software development workflow**.
