from models.person import Person


class Dietitian(Person):

    def __init__(self, firstname: str, lastname: str, phone_number: str,
                 company_address: str):
        super().__init__(firstname, lastname, phone_number)
        self._company_address = company_address

    @property
    def company_address(self) -> str:
        return self._company_address

    def __str__(self) -> str:
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s' % vars(self)[item] for item in vars(self))
        )
