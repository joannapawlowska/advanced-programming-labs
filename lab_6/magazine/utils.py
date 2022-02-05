class Utils:

    order_number = 0
    product_number = 0

    @staticmethod
    def generate_order_number() -> int:
        Utils.order_number += 1
        return Utils.order_number

    @staticmethod
    def generate_product_number() -> int:
        Utils.product_number += 1
        return Utils.product_number
