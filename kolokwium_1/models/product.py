from models.inventory import Inventory
from datetime import datetime


class Product:

    def __init__(self, product_name: str, price: float, last_modified: datetime,
                 description: str, inventory: Inventory):
        self._product_name = product_name
        self._price = price
        self._last_modified = last_modified
        self._description = description
        self._inventory = inventory

    @property
    def product_name(self):
        return self.product_name

    @property
    def price(self):
        return self.price

    @property
    def last_modified(self):
        return self.last_modified

    @property
    def description(self):
        return self.description

    @property
    def inventory(self):
        return self.inventory

    def __str__(self) -> str:
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s' % vars(self)[item] for item in vars(self))
        )

    def __repr__(self):
        return self.__str__()
