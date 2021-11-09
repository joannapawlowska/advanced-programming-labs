class Client:

    def __init__(self, firstname: str, lastname: str,
                 phone_number: str, address: str):
        self._firstname = firstname
        self._lastname = lastname
        self._phone_number = phone_number
        self._address = address

    @property
    def firstname(self):
        return self._firstname

    @property
    def lastname(self):
        return self._lastname

    @property
    def phone_number(self):
        return self._phone_number

    @property
    def address(self):
        return self._address

    def __str__(self) -> str:
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s' % vars(self)[item] for item in vars(self))
        )
