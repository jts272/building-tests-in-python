from datetime import date, timedelta


class Student:
    """
    A student class as a base for method testing
    """

    def __init__(self, first_name, last_name):
        # prepended underscore denotes read-only
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False

    # this decorator is used as this method gets data only
    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    def alert_santa(self):
        self.naughty_list = True

    # This method essentially creates a student.email property, thanks
    # to the @property decorator
    @property
    def email(self):
        return (
            f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"
        )

    def apply_extension(self, days):
        current_end = self.end_date
        extension = timedelta(days)
        extend_end = current_end + extension
        self.end_date = extend_end


# test = Student("John", "Doe")
# print(test.apply_extension(1))
