import pytest
from src.models import Product, Category

def test_product_init():
    p = Product(name="Laptop", description="Gaming laptop", price=1299.99, quantity=5)
    assert p.name == "Laptop"
    assert p.description == "Gaming laptop"
    assert p.price == 1299.99
    assert p.quantity == 5

def test_category_init_initial_counts():
    Category.total_categories = 0
    Category.total_products = 0

    c = Category(
        name="Electronics",
        description="Electronic devices",
        products=[
            Product("Phone", "Smartphone", 699.0, 10),
            Product("Headphones", "Noise cancelling", 199.99, 15),
        ]
    )

    assert c.name == "Electronics"
    assert c.description == "Electronic devices"
    assert isinstance(c.products, list)
    assert len(c.products) == 2
    assert Category.total_categories == 1
    assert Category.total_products == 2

def test_category_add_product_updates_counts():
    Category.total_categories = 0
    Category.total_products = 0

    c = Category(name="Books", description="Various books")
    assert Category.total_categories == 1
    assert Category.total_products == 0

    p = Product("Python 101", "Intro to Python", 29.99, 7)
    c.add_product(p)

    assert len(c.products) == 1
    assert Category.total_products == 1
