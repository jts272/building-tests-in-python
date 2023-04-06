import unittest
# import the function into the test file
from evens import even_number_of_evens


class TestEvens(unittest.TestCase):
    # pass statement to run without specifying the unit test module
    # (Placeholder code - Python expects some code after the ':')
    # Use this on first run to test the file
    # pass

    # # Use 'self' kw as we are in a class
    # def test_function_returns_True(self):
    #     # single assert
    #     self.assertTrue(even_number_of_evens([]))
    # This example passed when the function was set to return 'True'

    # ACTUAL TESTS -----------------------------------------------------
    # Test function must start with the word 'test'
    # Remember to pass in 'self'
    def test_throws_error_if_value_passed_is_not_list(self):
        self.assertRaises(TypeError, even_number_of_evens, 4)


    def test_values_in_list(self):
        self.assertEqual(even_number_of_evens([]), False)
        self.assertEqual(even_number_of_evens([2, 4]), True)
        # test only one even number passed in
        self.assertEqual(even_number_of_evens([2]), False)
        self.assertEqual(even_number_of_evens([1, 3, 5]), False)



# Run the file without specifying the unit test module
# if statement = 'Do this if the file is run directly'
if __name__ == "__main__":
    unittest.main()
