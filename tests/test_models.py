import pytest

from src.models import Category, LawnGrass, Product, Smartphone


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


def test_add_smartphone_to_category():
    cat = Category("Смартфоны")
    phone = Smartphone("iPhone", price=100000, quantity=5, model="14 Pro", memory=128, color="Black")
    cat.add_product(phone)
    assert cat.products[0].model == "14 Pro"


def test_add_lawngrass_to_category():
    cat = Category("Газон")
    grass = LawnGrass("Газонная трава", price=200, quantity=10, country="RU", germination_period="7", color="Green")
    cat.add_product(grass)
    assert cat.products[0].country == "RU"


def test_add_invalid_object_to_category():
    cat = Category("Смартфоны")
    with pytest.raises(TypeError):
        cat.add_product()


def test_add_different_classes_raises():
    a = Smartphone("iPhone", price=100000, quantity=1)
    b = LawnGrass("Газон", price=200, quantity=10)
    with pytest.raises(TypeError):
        _ = a + b


def test_add_same_class_products():
    a = Smartphone("iPhone", price=100000, quantity=2)
    b = Smartphone("Samsung", price=50000, quantity=3)
    assert a + b == 2*100000 + 3*50000


def test_mixin_output(capsys):
    Product("Test", "Desc", 100, 1)
    assert "Создан обьект Product c параметрами (), {}"
