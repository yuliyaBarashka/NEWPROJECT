from typing import Dict, List, Optional


class Product:
    product_count: int = 0

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name: str = name
        self.description: str = description
        self.__price: float = price
        self.quantity: int = quantity
        Product.product_count += 1

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, data: Dict, products_list: Optional[List["Product"]] = None):
        if products_list:
            for product in products_list:
                if product.name == data["name"]:
                    product.quantity += data["quantity"]
                    if data["price"] > product.price:
                        product.price = data["price"]
                    return product
        return cls(data["name"], data["description"], data["price"], data["quantity"])


class Category:
    total_categories: int = 0
    total_products: int = 0

    def __init__(self, name: str, description: str = "", products: Optional[List[Product]] = None):
        self.name: str = name
        self.description: str = description
        self.__products: List[Product] = products if products else []
        Category.total_categories += 1
        Category.total_products += len(self.__products)

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.total_products += 1

    @property
    def products(self) -> List[Product]:
        return self.__products
