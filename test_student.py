import unittest
from student import Student


class TestStudent(unittest.TestCase):
    def test_full_name(self):
        # create instance of the Student class in order to test it
        student = Student("John", "Doe")
        # test case - full name method displays correctly
        self.assertEqual(student.full_name, "John Doe")

    def test_alert_santa(self):
        student = Student("John", "Doe")
        student.alert_santa()

        self.assertTrue(student.naughty_list)

    def test_email_address(self):
        # create instance of the Student class in order to test it
        student = Student("John", "Doe")

        self.assertEqual(student.email, "john.doe@email.com")


if __name__ == "__main__":
    unittest.main()
