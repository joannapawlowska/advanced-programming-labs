from models.client import Client


class BusinessClient(Client):

    def __init__(self, firstname: str, lastname: str, phone_number: str,
                 address: str, company_address: str):
        super().__init__(firstname, lastname, phone_number, address)
        self._company_address = company_address

    @property
    def company_address(self):
        return self._company_address

    def __str__(self) -> str:
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s' % vars(self)[item] for item in vars(self))
        )
