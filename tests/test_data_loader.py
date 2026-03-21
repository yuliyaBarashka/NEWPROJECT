import json

import pytest

from src.data_loader import load_data_from_json
from src.models import Category


@pytest.fixture
def json_file(tmp_path):
    data = {
        "categories": [
            {
                "name": "Electronics",
                "description": "Electronic devices",
                "products": [
                    {
                        "name": "Phone",
                        "description": "Smartphone",
                        "price": 699,
                        "quantity": 10
                    },
                    {
                        "name": "Headphones",
                        "price": 199.99,
                        "quantity": 15
                    }
                ]
            }
        ]
    }

    file_path = tmp_path / "data.json"

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)

    return file_path


def test_load_data_from_json(json_file):
    Category.total_categories = 0
    Category.total_products = 0

    categories = load_data_from_json(json_file)

    assert len(categories) == 1
    category = categories[0]

    assert category.name == "Electronics"
    assert category.description == "Electronic devices"
    assert len(category.products) == 2

    product = category.products[0]
    assert product.name == "Phone"
    assert product.price == 699.0
    assert product.quantity == 10


def test_load_empty_categories(tmp_path):
    data = {"categories": []}

    file_path = tmp_path / "empty.json"

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)

    categories = load_data_from_json(file_path)

    assert categories == []


def test_category_without_products(tmp_path):
    data = {
        "categories": [
            {
                "name": "Books",
                "description": "Books category"
            }
        ]
    }

    file_path = tmp_path / "books.json"

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)

    categories = load_data_from_json(file_path)

    assert len(categories) == 1
    assert categories[0].products == []


def test_default_product_values(tmp_path):
    data = {
        "categories": [
            {
                "name": "Test",
                "products": [
                    {
                        "name": "Item"
                    }
                ]
            }
        ]
    }

    file_path = tmp_path / "defaults.json"

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)

    categories = load_data_from_json(file_path)

    product = categories[0].products[0]

    assert product.description == ""
    assert product.price == 0.0
    assert product.quantity == 0


def test_no_categories_key(tmp_path):
    data = {}

    file_path = tmp_path / "test.json"

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)

    result = load_data_from_json(file_path)

    assert result == []


def test_product_default_values(tmp_path):
    data = {
        "categories": [
            {
                "name": "Test",
                "products": [
                    {
                        "name": "Item"
                    }
                ]
            }
        ]
    }

    file_path = tmp_path / "test3.json"

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)

    result = load_data_from_json(file_path)

    product = result[0].products[0]

    assert product.description == ""
    assert product.price == 0.0
    assert product.quantity == 0
