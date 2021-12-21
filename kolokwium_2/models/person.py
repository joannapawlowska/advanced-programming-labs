class Person:

    def __init__(self, firstname: str, lastname: str, phone_number: str):
        self._firstname = firstname
        self._lastname = lastname
        self._phone_number = phone_number

    @property
    def firstname(self) -> str:
        return self._firstname

    @property
    def lastname(self) -> str:
        return self._lastname

    @property
    def phone_number(self) -> str:
        return self._phone_number

    def __str__(self) -> str:
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s' % vars(self)[item] for item in vars(self))
        )

    def __repr__(self):
        return self.__str__()
