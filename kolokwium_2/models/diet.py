class Diet:

    def __init__(self, name: str, duration_in_days: int,
                 price: float, kcal: int):
        self._name = name
        self._duration_in_days = duration_in_days
        self._price = price
        self._kcal = kcal

    @property
    def name(self) -> str:
        return self._name

    @property
    def duration_in_days(self) -> int:
        return self._duration_in_days

    @property
    def price(self) -> float:
        return self._price

    @property
    def kcal(self) -> int:
        return self._kcal

    def __str__(self) -> str:
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s' % vars(self)[item] for item in vars(self))
        )

    def __repr__(self):
        return self.__str__()
