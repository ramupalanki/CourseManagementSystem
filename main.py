from course_management_system.models import (
    Course,
    Enrollment,
    Mentor,
    Report,
    Student,
    User,
)


def main():
    print("=== COURSE MANAGEMENT SYSTEM ===\n")

    mentor = Mentor("Anita Rao", "anita@example.com", "Python & AI")
    student1 = Student("Ravi Kumar", "ravi@example.com")
    student2 = Student("Priya Sharma", "priya@example.com")

    python_course = Course("Python OOP Masterclass", 30)
    ai_course = Course("AI Fundamentals", 24)

    mentor.assign_course(python_course)
    mentor.assign_course(ai_course)

    enrollment1 = Enrollment(student1, python_course)
    enrollment2 = Enrollment(student2, python_course)
    enrollment3 = Enrollment(student1, ai_course)

    enrollment1.update_progress(75)
    enrollment2.update_progress(100)
    enrollment3.update_progress(25)

    users = [mentor, student1, student2]
    enrollments = [enrollment1, enrollment2, enrollment3]

    print("--- Users ---")
    Report.print_users(users)

    print("\n--- Courses ---")
    for course in [python_course, ai_course]:
        print(course.course_summary())

    print("\n--- Enrollments ---")
    Report.print_enrollments(enrollments)

    print("\n--- Student Progress ---")
    print(student1.get_progress())

    print("\n--- OOP Demonstration ---")
    print(f"Student role: {student1.get_role()}")
    print(f"Mentor role: {mentor.get_role()}")
    print(f"Valid email? {User.validate_email('student@example.com')}")


if __name__ == "__main__":
    main()
