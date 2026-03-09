from typing import List

class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = float(price)
        self.quantity = int(quantity)

    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price}, quantity={self.quantity})"


class Category:
    total_categories: int = 0
    total_products: int = 0

    def __init__(self, name: str, description: str, products: List[Product] = None):
        self.name = name
        self.description = description
        self.products = products if products is not None else []

        # обновляем счетчики
        Category.total_categories += 1
        initial_count = len(self.products)
        Category.total_products += initial_count

    def add_product(self, product: Product):
        self.products.append(product)
        Category.total_products += 1

    def __repr__(self):
        return f"Category(name={self.name!r}, products={len(self.products)})"
