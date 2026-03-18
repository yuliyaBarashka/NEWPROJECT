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


def test_str_product():
    prod = Product("iPhone", "Телефон", 100000, 5)
    assert str(prod) == "iPhone, 100000, руб. Остаток: 5 шт."


def test_str_category():
    cat = Category("Телефоны")
    prod1 = Product("iPhone", "Телефон", 100000, 5)
    prod2 = Product("Samsung", "Телефон", 50000, 10)
    cat.add_product(prod1)
    cat.add_product(prod2)
    assert str(cat) == "Телефоны, количество продуктов: 15 шт."


def test_add_products_sum():
    a = Product("A", "Desc", 100, 10)
    b = Product("B", "Desc", 200, 2)
    assert a + b == 1400
