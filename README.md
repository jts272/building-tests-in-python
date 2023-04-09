# building-tests-in-python

A repository to learn testing in Python, using unittest from the standard library

## Lifecycle of a test

When the `test_student.py` file is run in the Python interpreter, print statements
are used to show which tests run and in what order.

In general:

- setUp runs before each
- tearDown runs after each
- setUpClass runs before all
- tearDownClass runs after all

This is helpful in setting up test conditions once that can be re-used.

Note the correct usage of `cls` and `@classmethod` when setting up conditions
that affect the whole test class.
