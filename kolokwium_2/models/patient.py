from models.person import Person


class Patient(Person):

    def __init__(self, firstname: str, lastname: str, phone_number: str,
                 personal_address: str):
        super().__init__(firstname, lastname, phone_number)
        self._personal_address = personal_address

    @property
    def personal_address(self) -> str:
        return self._personal_address

    def __str__(self) -> str:
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s' % vars(self)[item] for item in vars(self))
        )
