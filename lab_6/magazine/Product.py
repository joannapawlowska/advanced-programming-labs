from magazine.utils import Utils


class Product:

    def __init__(self, name: str):
        self._name = name
        self._product_no = Utils.generate_product_number()

    def __str__(self) -> str:
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s' % vars(self)[item] for item in vars(self))
        )
