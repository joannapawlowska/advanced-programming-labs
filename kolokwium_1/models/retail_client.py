from models.client import Client


class RetailClient(Client):

    def __init__(self, firstname: str, lastname: str, phone_number: str,
                 address: str, client_number: int):
        super().__init__(firstname, lastname, phone_number, address)
        self._client_number = client_number

    @property
    def client_number(self):
        return self._client_number

    def __str__(self) -> str:
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s' % vars(self)[item] for item in vars(self))
        )
