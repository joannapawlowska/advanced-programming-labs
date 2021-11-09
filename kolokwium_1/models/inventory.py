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
        return self.address

    @property
    def phone_number(self):
        return self.phone_number

    @property
    def address2(self):
        return self.address2

    @property
    def info(self):
        return self.info

    @property
    def email(self):
        return self.email

    def __str__(self) -> str:
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s' % vars(self)[item] for item in vars(self))
        )

    def __repr__(self):
        return self.__str__()
