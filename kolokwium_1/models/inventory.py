class Inventory:

    def __init__(self, address: str, phone_number: str, address2: str,
                 info: str, email: str):
        self._address = address
        self._phone_number = phone_number
        self._address2 = address2
        self._info = info
        self._email = email

    @property
    def address(self):
        return self._address

    @property
    def phone_number(self):
        return self._phone_number

    @property
    def address2(self):
        return self._address2

    @property
    def info(self):
        return self._info

    @property
    def email(self):
        return self._email

    def __str__(self) -> str:
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s' % vars(self)[item] for item in vars(self))
        )

    def __repr__(self):
        return self.__str__()
