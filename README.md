# Course Management System

A production-style Python OOP mini-project that demonstrates core Object-Oriented Programming concepts while using a professional Git/GitHub workflow.

## 1. Problem Statement

Build a Course Management System where:

- Users can be represented as Students or Mentors.
- Mentors can be assigned to courses.
- Students can enroll in courses.
- Enrollment progress can be tracked from 0% to 100%.
- The application demonstrates inheritance, encapsulation, polymorphism, abstraction, instance methods, `@staticmethod`, and `@classmethod`.
- Development is managed using Git feature branches, meaningful commits, merges, and at least one Pull Request.

## 2. Architecture

```text
Course Management System
│
├── User (Abstract Base Class)
│   ├── Student
│   └── Mentor
│
├── Course
│
├── Enrollment
│
├── Report
│
├── main.py
│
└── tests/
    └── test_models.py
```

### Classes

| Class | Responsibility |
|---|---|
| `User` | Abstract base class for system users |
| `Student` | Stores student information and enrollments |
| `Mentor` | Stores mentor expertise and assigned courses |
| `Course` | Stores course information and mentor |
| `Enrollment` | Connects a student to a course and tracks progress |
| `Report` | Prints users and enrollment information |

## 3. OOP Concepts Demonstrated

### 3.1 Inheritance

`Student` and `Mentor` inherit from `User`.

```python
class Student(User):
    ...

class Mentor(User):
    ...
```

This allows both classes to reuse common user functionality.

### 3.2 Abstraction

`User` is an abstract base class and requires subclasses to implement `get_role()`.

```python
class User(ABC):

    @abstractmethod
    def get_role(self):
        raise NotImplementedError
```

### 3.3 Encapsulation

Private attributes are used for internal state.

```python
self.__enrollments = []
self.__progress = 0
```

Progress can only be changed through the validated method:

```python
enrollment.update_progress(75)
```

### 3.4 Polymorphism

Both `Student` and `Mentor` implement `get_role()` differently.

```python
student.get_role()   # Student
mentor.get_role()    # Mentor
```

`Report.print_users()` can work with both because both are `User` objects.

### 3.5 Instance Methods

Instance methods operate on a specific object.

```python
course.course_summary()
student.get_progress()
enrollment.update_progress(75)
```

### 3.6 `@staticmethod`

Email validation does not require an object.

```python
User.validate_email("student@example.com")
```

### 3.7 `@classmethod`

Class methods are used for ID generation.

```python
Student._generate_id()
Course._generate_course_id()
```

The class owns the sequence rather than an individual object.

## 4. Features

- Student registration
- Mentor creation
- Course creation
- Mentor-course assignment
- Student enrollment
- Progress tracking
- Enrollment status
- Email validation
- Automatic IDs
- Console reports
- Unit tests
- No external dependencies

## 5. Requirements

- Python 3.10 or later
- Git
- GitHub account

## 6. Installation

Clone the repository:

```bash
git clone https://github.com/<YOUR_USERNAME>/course-management-system.git
cd course-management-system
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Activate it on Linux/macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

There are currently no third-party dependencies.

## 7. Execution

Run the application:

```bash
python main.py
```

Example output:

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

## 8. Run Tests

Run the built-in unit tests:

```bash
python -m unittest discover -s tests -v
```

Expected result:

```text
Ran 6 tests

OK
```

## 9. Git/GitHub Workflow

The project should be developed using feature branches rather than making every change directly on `main`.

### Step 1: Initialize repository

```bash
git init
git branch -M main
git add .
git commit -m "chore: initialize course management project"
```

### Step 2: Connect GitHub

Create a public repository named:

```text
course-management-system
```

Then:

```bash
git remote add origin https://github.com/<YOUR_USERNAME>/course-management-system.git
git push -u origin main
```

### Step 3: Create feature branch

```bash
git checkout -b feature/user-course-models
```

Make the User, Student, Mentor and Course changes.

```bash
git add .
git commit -m "feat: add user student mentor and course models"
git push -u origin feature/user-course-models
```

### Step 4: Create Pull Request

On GitHub:

1. Open the repository.
2. Select **Pull requests**.
3. Click **New pull request**.
4. Base: `main`.
5. Compare: `feature/user-course-models`.
6. Title: `feat: add user student mentor and course models`.
7. Add a description explaining the implementation.
8. Create the Pull Request.
9. Review the changes.
10. Merge the Pull Request into `main`.

Record the Pull Request URL for submission.

### Step 5: Add enrollment functionality

After merging the first feature:

```bash
git checkout main
git pull origin main
git checkout -b feature/enrollment-progress
```

Implement `Enrollment` and progress tracking.

```bash
git add .
git commit -m "feat: add enrollment and progress tracking"
git push -u origin feature/enrollment-progress
```

Create and merge a second Pull Request.

### Step 6: Add tests and documentation

```bash
git checkout main
git pull origin main
git checkout -b feature/tests-readme
```

Add unit tests and README improvements.

```bash
git add .
git commit -m "test: add course management unit tests"
git add README.md
git commit -m "docs: add project architecture and usage guide"
git push -u origin feature/tests-readme
```

Create the final Pull Request and merge it.

## 10. Meaningful Commit History

A good final history can look like:

```text
docs: add project architecture and usage guide
test: add course management unit tests
feat: add enrollment and progress tracking
feat: add user student mentor and course models
chore: initialize course management project
```

Check it with:

```bash
git log --oneline --graph --decorate --all
```

## 11. Demonstrating a Git Merge Conflict

To demonstrate conflict resolution as an additional Git learning exercise:

```bash
git checkout main
git checkout -b feature/report-a
```

Modify the same line in `main.py` and commit:

```bash
git add main.py
git commit -m "feat: update application heading"
git checkout main
```

Create another branch from the original base:

```bash
git checkout -b feature/report-b
```

Change the same line differently and commit:

```bash
git add main.py
git commit -m "feat: customize application heading"
git checkout main
```

Merge the first branch:

```bash
git merge feature/report-a
```

Then merge the second:

```bash
git merge feature/report-b
```

Git should report a conflict.

Open `main.py` and look for:

```text
<<<<<<< HEAD
your current version
=======
incoming version
>>>>>>> feature/report-b
```

Choose the desired final code, remove the conflict markers, then:

```bash
git add main.py
git commit -m "fix: resolve merge conflict in application heading"
```

Push the resolved history:

```bash
git push origin main
```

## 12. Production-Ready Checklist

Before submission:

- [ ] Code runs successfully.
- [ ] Unit tests pass.
- [ ] No hard-coded local paths.
- [ ] No secrets or passwords committed.
- [ ] `.gitignore` is present.
- [ ] README is complete.
- [ ] Feature branches were used.
- [ ] Meaningful commits exist.
- [ ] At least one Pull Request was created and merged.
- [ ] GitHub repository is public.
- [ ] Repository URL is recorded.
- [ ] Pull Request URL is recorded.

## 13. Submission

Submit these two URLs:

```text
Repository:
https://github.com/<YOUR_USERNAME>/course-management-system

Pull Request:
https://github.com/<YOUR_USERNAME>/course-management-system/pull/1
```

Replace `<YOUR_USERNAME>` and the PR number with the actual values from GitHub.

## 14. Final Explanation

The system uses an abstract `User` class as the common parent. `Student` and `Mentor` inherit from it and provide their own role implementation, demonstrating inheritance and polymorphism. Private attributes such as enrollment lists and progress demonstrate encapsulation. The abstract `get_role()` method demonstrates abstraction.

The project also uses instance methods for object behavior, a static method for email validation, and class methods for ID generation. `Enrollment` connects students and courses and controls progress updates through validation.

Git feature branches separate changes into logical units. Meaningful commits make the history understandable, while Pull Requests provide a review point before changes are merged into `main`.
