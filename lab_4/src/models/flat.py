from src.models.property import Property


class Flat(Property):

    def __init__(self, area: str, rooms: int, price: float, address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self._floor = floor

    def __str__(self) -> str:
        return '%s(%s)' % (type(self).__name__, ', '.join('%s' % vars(self)[item] for item in vars(self)))
