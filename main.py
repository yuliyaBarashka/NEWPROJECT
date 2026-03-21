from src.models import Category, Smartphone, LawnGrass

if __name__ == '__main__':
    smartphone1 = Smartphone(name="Samsung Galaxy S23 Ultra",
                             description="256GB, Серый цвет, 200MP камера",
                             price=180000.0,
                             quantity=5,
                             efficiency=95.5,
                             model="S23 Ultra",
                             memory=256,
                             color="Серый")
    smartphone2 = Smartphone(name="Iphone 15",
                             description="512GB, Gray space",
                             price=210000.0,
                             quantity=8,
                             efficiency=98.2,
                             model="15",
                             memory=512,
                             color="Gray space")
    smartphone3 = Smartphone(name="Xiaomi Redmi Note 11",
                             description="1024GB, Синий",
                             price=31000.0,
                             quantity=14,
                             efficiency=90.3,
                             model="Note 11",
                             memory=1024,
                             color="Синий")

    print(smartphone1.name)
    print(smartphone1.description)
    print(smartphone1.price)
    print(smartphone1.quantity)
    print(smartphone1.efficiency)
    print(smartphone1.model)
    print(smartphone1.memory)
    print(smartphone1.color)

    print(smartphone2.name)
    print(smartphone2.description)
    print(smartphone2.price)
    print(smartphone2.quantity)
    print(smartphone2.efficiency)
    print(smartphone2.model)
    print(smartphone2.memory)
    print(smartphone2.color)

    print(smartphone3.name)
    print(smartphone3.description)
    print(smartphone3.price)
    print(smartphone3.quantity)
    print(smartphone3.efficiency)
    print(smartphone3.model)
    print(smartphone3.memory)
    print(smartphone3.color)

    grass1 = LawnGrass(name="Газонная трава",
                       description="Элитная трава для газона",
                       price=500.0,
                       quantity=20,
                       country="Россия",
                       germination_period="7 дней",
                       color="Зеленый")
    grass2 = LawnGrass(name="Газонная трава 2",
                       description="Выносливая трава",
                       price=450.0,
                       quantity=15,
                       country="США",
                       germination_period="5 дней",
                       color="Темно-зеленый")

    print(grass1.name)
    print(grass1.description)
    print(grass1.price)
    print(grass1.quantity)
    print(grass1.country)
    print(grass1.germination_period)
    print(grass1.color)

    print(grass2.name)
    print(grass2.description)
    print(grass2.price)
    print(grass2.quantity)
    print(grass2.country)
    print(grass2.germination_period)
    print(grass2.color)

    smartphone_sum = smartphone1 + smartphone2
    print(smartphone_sum)

    grass_sum = grass1 + grass2
    print(grass_sum)

    try:
        invalid_sum = smartphone1 + grass1
    except TypeError:
        print("Возникла ошибка TypeError при попытке сложения")
    else:
        print("Не возникла ошибка TypeError при попытке сложения")

    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
    category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])

    category_smartphones.add_product(smartphone3)

    print(category_smartphones.products)

    print(Category.total_categories)

    try:
        category_smartphones.add_product("Not a product")  # type: ignore
    except TypeError:
        print("Возникла ошибка TypeError при добавлении не продукта")
    else:
        print("Не возникла ошибка TypeError при добавлении не продукта")
