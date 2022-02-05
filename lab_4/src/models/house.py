from src.models.property import Property


class House(Property):

    def __init__(self, area: str, rooms: int, price: float,
                 address: str, plot: int):
        super().__init__(area, rooms, price, address)
        self._plot = plot

    def __str__(self) -> str:
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s' % vars(self)[item] for item in vars(self))
        )
