from models.client import Client
from models.product import Product
from datetime import datetime


class Order:

    # _order_id: int
    # _date: datetime
    # _products: list[Product]
    # _status: str
    # _client: Client

    def __init__(self, order_id: int, date: datetime, products: list[Product], status: str, client: Client):
        self._order_id = order_id
        self._date = date
        self._products = products
        self._status = status
        self._client = client

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, order_id: int):
        self._order_id = order_id

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date: datetime):
        self._date = date

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, products: list[Product]):
        self._products = products

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status: str):
        self._status = status

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, client: Client):
        _client = client

    def __str__(self) -> str:
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s' % vars(self)[item] for item in vars(self))
        )

    def calculate_total_price(self):
        total_price = 0
        for p in self._products:
            total_price += p.price
        return total_price

    def get_client_address(self):
        return self._client.address
