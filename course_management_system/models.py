from abc import ABC, abstractmethod
from datetime import datetime


class User(ABC):
    """Abstract base class representing a system user."""

    _next_id = 1000

    def __init__(self, name: str, email: str):
        self.user_id = self._generate_id()
        self.name = name
        self.email = email

    @classmethod
    def _generate_id(cls) -> int:
        """Generate a unique user ID."""
        user_id = User._next_id
        User._next_id += 1
        return user_id

    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate an email address without creating an object."""
        return "@" in email and "." in email.split("@")[-1]

    @abstractmethod
    def get_role(self) -> str:
        """Return the user's role."""
        raise NotImplementedError

    def display_profile(self) -> str:
        return f"[{self.user_id}] {self.name} <{self.email}> - {self.get_role()}"


class Student(User):
    """Student derived from User."""

    def __init__(self, name: str, email: str):
        if not self.validate_email(email):
            raise ValueError("Invalid email address.")
        super().__init__(name, email)
        self.__enrollments = []

    def get_role(self) -> str:
        return "Student"

    def add_enrollment(self, enrollment: "Enrollment") -> None:
        self.__enrollments.append(enrollment)

    def get_enrollments(self) -> tuple:
        """Return a read-only view of enrollments."""
        return tuple(self.__enrollments)

    def get_progress(self) -> str:
        if not self.__enrollments:
            return "No active enrollments."
        lines = [
            f"{e.course.title}: {e.progress}%"
            for e in self.__enrollments
        ]
        return "\n".join(lines)


class Mentor(User):
    """Mentor derived from User."""

    def __init__(self, name: str, email: str, expertise: str):
        if not self.validate_email(email):
            raise ValueError("Invalid email address.")
        super().__init__(name, email)
        self.expertise = expertise
        self.__courses = []

    def get_role(self) -> str:
        return "Mentor"

    def assign_course(self, course: "Course") -> None:
        if course not in self.__courses:
            self.__courses.append(course)
            course.set_mentor(self)

    def get_courses(self) -> tuple:
        return tuple(self.__courses)


class Course:
    """Represents a course managed by a mentor and taken by students."""

    _next_id = 1

    def __init__(self, title: str, duration_hours: int):
        if duration_hours <= 0:
            raise ValueError("Duration must be greater than zero.")
        self.course_id = self._generate_course_id()
        self.title = title
        self.duration_hours = duration_hours
        self.__mentor = None

    @classmethod
    def _generate_course_id(cls) -> int:
        course_id = cls._next_id
        cls._next_id += 1
        return course_id

    def set_mentor(self, mentor: Mentor) -> None:
        self.__mentor = mentor

    def get_mentor(self):
        return self.__mentor

    def course_summary(self) -> str:
        mentor_name = self.__mentor.name if self.__mentor else "Not assigned"
        return (
            f"Course #{self.course_id}: {self.title} | "
            f"{self.duration_hours} hours | Mentor: {mentor_name}"
        )


class Enrollment:
    """Connects a student with a course and tracks progress."""

    def __init__(self, student: Student, course: Course):
        self.student = student
        self.course = course
        self.__progress = 0
        self.enrolled_at = datetime.now()
        student.add_enrollment(self)

    @property
    def progress(self) -> int:
        return self.__progress

    def update_progress(self, percentage: int) -> None:
        """Encapsulated progress update with validation."""
        if not 0 <= percentage <= 100:
            raise ValueError("Progress must be between 0 and 100.")
        self.__progress = percentage

    def status(self) -> str:
        if self.__progress == 100:
            return "Completed"
        if self.__progress > 0:
            return "In Progress"
        return "Not Started"

    def __str__(self) -> str:
        return (
            f"{self.student.name} -> {self.course.title} | "
            f"{self.progress}% | {self.status()}"
        )


class Report:
    """Demonstrates polymorphism through a common reporting interface."""

    @staticmethod
    def print_users(users: list[User]) -> None:
        for user in users:
            print(user.display_profile())

    @staticmethod
    def print_enrollments(enrollments: list[Enrollment]) -> None:
        for enrollment in enrollments:
            print(enrollment)
