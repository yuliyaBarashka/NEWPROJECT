 Проект: Виджет банковских операций
## 📌 Описание проекта
Проект представляет собой модель интернет магазина с использованием ООП. Реализованы классы товаров,
категории, а также механизмы работы с данными валидации.

## 🗂 Структура проекта
HOMEWORKE9_2/\
├── data/\
│   ├── products.json\
│\
├── src/\
│   ├── models.py          # Классы Product, Category, LawnGrass, Smartphone, InitMixin, BaseProduct(ABC)\
│   ├── data_loader.py        # Выгрузка Json\
│   └── __init __.py\
│\
├── tests/\
│   ├── test_models.py       # Test for models.py\
│   └── test_data_loader.py       # Test for data_loader.py\
│\
├── HTMLres/              # HTML-отчёт покрытия тестами\
│   └── index.html\
│\
├── pyproject.toml\
├── poetry.lock\
├── README.md\
└── requirements.txt\

## Product
Класс описывает товар  

Атрибуты:
- name
- description
- price
- quntity

Примеры создания товара:

product = Product(\
   name="Laptop",\
   description="Gaming laptop",\
   price=1299.99,\
   quantity=5\
)

## Category
Класс описывает товар  

Атрибуты:
- name
- description
- products

Также класс хранит статистику:
- total_category
- total_products

Примеры создания товара:

category = Category(\
   name="Laptop",\
   description="Gaming laptop",\
   products=[],\
)\

#### Добавление товара в категорию:
category.add_product(product)

## Smartphone
Класс описывает смартфон  

Атрибуты:
- name
- price
- quantity
- model
- description
- efficiency
- memory
- color

## LawnGrass
Класс описывает газон  

## BaseProduct
Абстрактный базовый класс.

Содержит:
- __str
- __add

## InitMixin
Выводит информацию при создании обьекта, показывает класс и переданные параметры.



## ⚙️ Установка и запуск
### 1️⃣ Клонирование репозитория
git clone <url_репозитория>
cd HOMEWORKE9_2
### 2️⃣ Установка зависимостей
poetry install

### 🧪 Тестирование
В проекте используются pytest, pytest-cov, параметризация и фикстуры.\
Запуск тестов\
poetry run pytest\
Проверка покрытия кода\
poetry run python -m pytest --cov=src --cov-report=html\
После выполнения команды будет создана папка htmlcov.\
Для просмотра отчёта открой файл:\
htmlcov/index.html\
Покрытие кода тестами — не менее 80%.\

## 🛠 Используемые технологии
Python 3.14\
Poetry\
Pytest\
Pytest-cov\

