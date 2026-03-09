import json
from typing import Dict, List


def load_data_from_json(path: str):
    with open(path, 'r', encoding='utf-8') as f:
        raw = json.load(f)

    categories = []
    for cat in raw.get("categories", []):
        products = []
        for prod in cat.get("products", []):
            products.append(Product(
                name=prod["name"],
                description=prod.get("description", ""),
                price=float(prod.get("price", 0)),
                quantity=int(prod.get("quantity", 0)),
            ))
        categories.append(Category(
            name=cat["name"],
            description=cat.get("description", ""),
            products=products
        ))
    return categories
