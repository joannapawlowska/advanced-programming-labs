class Library:

    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: str):
        self._city = city
        self._street = street
        self._zip_code = zip_code
        self._open_hours = open_hours
        self._phone = phone

    def __str__(self) -> str:
        return '%s(%s)' % (type(self).__name__, ', '.join('%s' % vars(self)[item] for item in vars(self)))
