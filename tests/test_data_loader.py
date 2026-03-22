import json

import pytest

from src.data_loader import load_data_from_json
from src.models import Category, LawnGrass, Product, Smartphone


@pytest.fixture
def json_file(tmp_path):
    data = {
        "categories": [
            {
                "name": "Electronics",
                "description": "Electronic devices",
                "products": [
                    {"name": "Phone", "description": "Smartphone", "price": 699, "quantity": 10},
                    {"name": "Headphones", "price": 199.99, "quantity": 15}
                ]
            }
        ]
    }

    file_path = tmp_path / "data.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)

    return file_path


def test_load_data_from_json(json_file):
    categories = load_data_from_json(str(json_file))

    assert len(categories) == 1
    category = categories[0]

    assert category.name == "Electronics"
    assert len(category.products) == 2

    product = category.products[0]
    assert product.name == "Phone"
    assert product.price == 699.0
    assert product.quantity == 10


def test_empty_data(tmp_path):
    file_path = tmp_path / "empty.json"
    with open(file_path, "w") as f:
        json.dump({}, f)

    result = load_data_from_json(str(file_path))
    assert result == []


def test_product_defaults(tmp_path):
    data = {"categories": [{"name": "Test", "products": [{"name": "Item"}]}]}
    file_path = tmp_path / "data.json"

    with open(file_path, "w") as f:
        json.dump(data, f)

    result = load_data_from_json(str(file_path))
    product = result[0].products[0]

    assert product.description == ""
    assert product.price == 0.0
    assert product.quantity == 0


def test_new_product_updates_existing():
    existing = [Product(name="Widget", price=10.0, quantity=2)]
    data = {"name": "Widget", "price": 12.0, "quantity": 3}

    prod = Product.new_product(data, products_list=existing)

    assert prod.quantity == 5
    assert prod.price == 12.0


def test_new_product_creates_new():
    data = {"name": "New", "price": 5.0, "quantity": 1}
    prod = Product.new_product(data)

    assert isinstance(prod, Product)
    assert prod.name == "New"


def test_price_setter():
    prod = Product(name="Test", price=100.0, quantity=1)

    prod.price = -10
    assert prod.price == 100.0


def test_price_decrease(monkeypatch):
    prod = Product(name="Test", price=100.0, quantity=1)

    monkeypatch.setattr("builtins.input", lambda _: "n")
    prod.price = 50

    assert prod.price == 100.0


def test_add_products():
    a = Product("A", "Desc", 100, 10)
    b = Product("B", "Desc", 200, 2)

    assert a + b == 1400


def test_add_same_class():
    a = Smartphone(name="iPhone", price=100000, quantity=2)
    b = Smartphone(name="Samsung", price=50000, quantity=3)

    assert a + b == 2 * 100000 + 3 * 50000


def test_add_different_classes():
    a = Smartphone(name="iPhone", price=100000, quantity=1)
    b = LawnGrass(name="Grass", price=200, quantity=10)

    with pytest.raises(TypeError):
        _ = a + b


def test_category():
    p1 = Product(name="A", price=10.0, quantity=1)
    p2 = Product(name="B", price=20.0, quantity=2)

    cat = Category("Test", products=[p1, p2])

    assert len(cat.products) == 2
    assert cat.total_categories == 3


def test_category_add_invalid():
    cat = Category("Test")

    with pytest.raises(TypeError):
        cat.add_product("wrong")


def test_iterator():
    p1 = Product(name="A", price=1.0, quantity=1)
    p2 = Product(name="B", price=2.0, quantity=2)

    cat = Category("Test", products=[p1, p2])

    assert list(cat) == [p1, p2]


def test_mixin_output(capsys):
    Product(name="Test", price=1.0, quantity=1)
    assert "Создан оьект Product c gfhfvtnhfvb: (), {} "
