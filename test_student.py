import unittest
# API mocking requirement for success and failure states
from unittest.mock import patch
from student import Student


class TestStudent(unittest.TestCase):

    # Unused setUpClass for demonstration purposes
    # Note this takes reference to cls, as it is a class method that
    # affects the whole class, not just the particular instance like
    # self would
    # Note use also of the @classmethod decorator. This works together
    # with the cls argument to make this function act upon the whole
    # class
    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    # As expected for the tearDownClass
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

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

    def test_apply_extension(self):
        print("test_apply_extension")
        # Variables to compare created inside the test, not inside the
        # actual class method
        current_end = self.student.end_date
        self.student.apply_extension(1)
        self.assertGreater(self.student.end_date, current_end)

    def test_course_schedule_api_ok(self):
        # Set context manager
        # Mocking get request
        # mocked_get object uses the student import
        with patch("student.requests.get") as mocked_get:
            # Set values explicitly as there is no real API call
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            # Var to store the return value of the given class method
            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")
            # Alternatively:
            self.assertEqual(schedule, mocked_get.return_value.text)

    def test_course_schedule_api_fail(self):
        with patch("student.requests.get") as mocked_get:
            # Set values explicitly as there is no real API call
            mocked_get.return_value.ok = False
            # This string is gleaned from the else block of the
            # course_schedule() response request
            mocked_get.return_value.text = (
                "Something went wrong with the request"
            )

            # Var to store the return value of the given class method
            schedule = self.student.course_schedule()
            self.assertEqual(schedule, mocked_get.return_value.text)


if __name__ == "__main__":
    unittest.main()
