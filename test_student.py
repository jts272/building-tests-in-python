import unittest
from student import Student


class TestStudent(unittest.TestCase):

    # DRY principle - setup test conditions at top of class for later
    # Note use of camelCase
    def setUp(self):
        print("setUp")
        # This creates an instance variable. All further references to
        # student must be prepended with self
        self.student = Student("John", "Doe")

    def tearDown(self):
        # Not actually used in this test suite, but printed to show when
        # it runs in the testing procedure
        print("tearDown")

    def test_full_name(self):
        # print the currently tested function
        print("test_full_name")
        # student class instantiated in setUp function
        # test case - full name method displays correctly
        self.assertEqual(self.student.full_name, "John Doe")

    def test_email_address(self):
        print("test_email_address")
        self.assertEqual(self.student.email, "john.doe@email.com")

    def test_alert_santa(self):
        print("test_alert_santa")
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)


if __name__ == "__main__":
    unittest.main()
