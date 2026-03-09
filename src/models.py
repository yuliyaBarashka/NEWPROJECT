from typing import List, Optional


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

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None):
        self.name = name
        self.description = description
        self.products = products if products is not None else []

        Category.total_categories += 1
        Category.total_products += len(self.products)

    def add_product(self, product: Product):
        self.products.append(product)
        Category.total_products += 1

    def __repr__(self):
        return f"Category(name={self.name!r}, products={len(self.products)})"
