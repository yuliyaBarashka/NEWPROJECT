from typing import List, Optional, Dict


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = float(price)  # приватный атрибут цены
        self.quantity = int(quantity)

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if value > 0:
            self._price = float(value)
        else:
            print("Цена не должна быть нулевая или отрицательная")

    def __repr__(self):
        return f"Product(name={self.name!r}, price={self._price}, quantity={self.quantity})"


class Category:
    total_categories: int = 0
    total_products: int = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None):
        self.name = name
        self.description = description
        self.__products: List[Product] = products if (products is not None) else []

        Category.total_categories += 1
        Category.total_products += len(self.__products)

    # Задача 1: добавление продукта в приватный список через метод
    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.total_products += 1

    # Задача 2: геттер для приватного атрибута продуктов
    @property
    def products(self) -> str:
        lines = []
        for p in self.__products:
            lines.append(f"{p.name}, {p.price:.0f} руб. Остаток: {p.quantity} шт.\n")
        return "".join(lines)

    # Задача 3: класс-метод new_product
    @classmethod
    def new_product(cls, data: Dict) -> 'Product':
        # ожидаем словарь с ключами: name, description, price, quantity
        name = data.get("name")
        description = data.get("description", "")
        price = data.get("price", 0.0)
        quantity = data.get("quantity", 0)
        return Product(name=name, description=description, price=price, quantity=quantity)

    def __repr__(self):
        return f"Category(name={self.name!r}, products={len(self.__products)})"