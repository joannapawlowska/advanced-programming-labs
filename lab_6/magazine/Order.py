from magazine.Product import Product
from magazine.utils import Utils


class Order:

    def __init__(self, product: Product):
        self._product = product
        self._order_no = Utils.generate_order_number()
