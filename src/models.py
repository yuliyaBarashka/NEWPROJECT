from typing import Dict, List, Optional


class Product:
    product_count: int = 0

    def __init__(self, name: str = "", description: str = "", price: float = 0.0, quantity: int = 0):
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
                    product.quantity += data.get("quantity", 0)
                    if data.get("price", 0) > product.price:
                        product.price = data["price"]
                    return product
        return cls(
            data["name"],
            data.get("description", ""),
            data.get("price", 0.0),
            data.get("quantity", 0)
        )

    def __str__(self):
        return f"{self.name}, {self.__price}, руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return (self.price * self.quantity) + (other.price * other.quantity)


class Category:
    total_categories: int = 0
    total_products: int = 0

    def __init__(self, name: str, description: str = "", products: Optional[List[Product]] = None):
        self.name: str = name
        self.description: str = description
        self.__products: List[Product] = products if products else []
        Category.total_categories += 1
        Category.total_products += sum(p.quantity for p in self.__products)
        self._iter_index = 0

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.total_products += product.quantity

    @property
    def products(self) -> List[Product]:
        # Возвращаем список объектов, чтобы старые тесты работали
        return self.__products

    def products_str(self) -> str:
        # Метод для строкового представления всех продуктов
        return "\n".join(str(p) for p in self.__products)

    def __str__(self):
        total_quantity = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    # Итератор для Category
    def __iter__(self):
        self._iter_index = 0
        return self

    def __next__(self):
        if self._iter_index < len(self.__products):
            prod = self.__products[self._iter_index]
            self._iter_index += 1
            return prod
        raise StopIteration
