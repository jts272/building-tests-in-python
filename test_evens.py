import unittest
# import the function into the test file
from evens import even_number_of_evens


class TestEvens(unittest.TestCase):
    # pass statement to run without specifying the unit test module
    # (Placeholder code - Python expects some code after the ':')
    # Use this on first run to test the file
    pass

    # # Use 'self' kw as we are in a class
    # def test_function_returns_True(self):
    #     # single assert
    #     self.assertTrue(even_number_of_evens([]))


# Run the file without specifying the unit test module
# if statement = 'Do this if the file is run directly'
if __name__ == "__main__":
    unittest.main()
