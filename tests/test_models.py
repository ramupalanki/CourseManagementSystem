import unittest

from course_management_system.models import Course, Enrollment, Mentor, Student, User


class TestCourseManagementSystem(unittest.TestCase):

    def setUp(self):
        self.mentor = Mentor("Anita Rao", "anita@example.com", "Python")
        self.student = Student("Ravi Kumar", "ravi@example.com")
        self.course = Course("Python OOP", 20)

    def test_inheritance(self):
        self.assertIsInstance(self.student, User)
        self.assertIsInstance(self.mentor, User)

    def test_email_validation_static_method(self):
        self.assertTrue(User.validate_email("test@example.com"))
        self.assertFalse(User.validate_email("invalid-email"))

    def test_class_method_id_generation(self):
        student2 = Student("Priya", "priya@example.com")
        self.assertNotEqual(self.student.user_id, student2.user_id)

    def test_private_enrollment_data(self):
        enrollment = Enrollment(self.student, self.course)
        self.assertEqual(len(self.student.get_enrollments()), 1)
        self.assertEqual(enrollment.progress, 0)

    def test_progress_validation(self):
        enrollment = Enrollment(self.student, self.course)
        enrollment.update_progress(50)
        self.assertEqual(enrollment.progress, 50)
        with self.assertRaises(ValueError):
            enrollment.update_progress(101)

    def test_course_assignment(self):
        self.mentor.assign_course(self.course)
        self.assertEqual(self.course.get_mentor(), self.mentor)
        self.assertIn(self.course, self.mentor.get_courses())


if __name__ == "__main__":
    unittest.main()
