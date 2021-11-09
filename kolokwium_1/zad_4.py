from models.product import Product
from models.order import Order
from models.retail_client import RetailClient
from models.inventory import Inventory
from datetime import datetime

client = RetailClient("tom", "brown", "098765432", "23, Brighton 76H6G", 231)
inventory = Inventory("34, Brighton 76H6G", "876098543",
                      "34, London HU7654", "empty", "inventory@mail.com")
product1 = Product("pc", 4500, datetime(2021, 11, 9), "empty", inventory)
product2 = Product("headphones", 600.912, datetime(2021, 10, 12),
                   "none", inventory)
order = Order()
order.order_id = 23
order.client = client
order.date = datetime(2021, 7, 3)
order.products = [product1, product2]
order.status = "SEND"

print(order)
