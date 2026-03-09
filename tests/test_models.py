import pytest
from src.models import Category, Product


@pytest.fixture
def sample_product():
    return Product(
        name="Laptop",
        description="Gaming laptop",
        price=1299.99,
        quantity=5
    )


@pytest.fixture
def sample_category():
    Category.total_categories = 0
    Category.total_products = 0

    return Category(
        name="Electronics",
        description="Electronic devices",
        products=[
            Product("Phone", "Smartphone", 699.0, 10),
            Product("Headphones", "Noise cancelling", 199.99, 15),
        ]
    )


def test_product_init(sample_product):
    assert sample_product.name == "Laptop"
    assert sample_product.description == "Gaming laptop"
    assert sample_product.price == 1299.99
    assert sample_product.quantity == 5


def test_category_init_initial_counts(sample_category):
    assert sample_category.name == "Electronics"
    assert sample_category.description == "Electronic devices"
    assert isinstance(sample_category.products, list)
    assert len(sample_category.products) == 2
    assert Category.total_categories == 1
    assert Category.total_products == 2


@pytest.fixture
def empty_category():
    Category.total_categories = 0
    Category.total_products = 0
    return Category(name="Books", description="Various books")


def test_category_add_product_updates_counts(empty_category):
    assert Category.total_categories == 1
    assert Category.total_products == 0

    p = Product("Python 101", "Intro to Python", 29.99, 7)
    empty_category.add_product(p)

    assert len(empty_category.products) == 1
    assert Category.total_products == 1
