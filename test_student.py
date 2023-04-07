import unittest
from student import Student


class TestStuden(unittest.TestCase):

    def test_full_name(self):
        # create instance of the Student class in order to test it
        student = Student("John", "Doe")
        # test case - full name method displays correctly
        self.assertEqual(student.full_name, "John Doe")




if __name__ == "__main__":
    unittest.main()
