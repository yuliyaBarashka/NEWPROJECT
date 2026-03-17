from src.models import Category, Product


def test_add_product():
    cat = Category("Телефоны", "Описание")
    prod = Product("iPhone", "Телефон", 100000, 5)

    cat.add_product(prod)

    assert any(p.name.lower() == "iphone".lower() for p in cat.products)


def test_price_setter_invalid():
    prod = Product("Test", "Desc", 100, 1)
    prod.price = -10

    assert prod.price == 100


def test_new_product_duplicate():
    existing = Product("Samsung", "Телефон", 40000, 5)

    data = {
        "name": "Samsung",
        "description": "Телефон",
        "price": 60000,
        "quantity": 3,
    }

    products = [existing]

    prod = Product.new_product(data, products)

    assert prod.quantity == 8
    assert prod.price == 60000
