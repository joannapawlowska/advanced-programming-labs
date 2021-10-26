import datetime


class Employee:

    def __init__(self, first_name: str, last_name: str, hire_date: datetime, birth_date: datetime, city: str,
                 street: str, zip_code: str, phone: str):
        self._first_name = first_name
        self._last_name = last_name
        self._hire_date = hire_date
        self._birth_date = birth_date
        self._city = city
        self._street = street
        self._zip_code = zip_code
        self._phone = phone

    def __str__(self) -> str:
        return '%s(%s)' % (type(self).__name__, ', '.join('%s' % vars(self)[item] for item in vars(self)))
