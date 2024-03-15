import peewee
from models import Category, Product
import random

def add_category(name):
    try:
        obj = Category(title = name.lower().strip())
        obj.save()
        print(f'Сохранили категории {obj} - {obj.title}')

    except (peewee.IntegrityError, peewee.IntegrityError):
        print (f'{name.lower().strip()} - эта категория уже существует')
        

# add_category('laptops')
# add_category('  pc  ')
# add_category('Sony Playstations')
# add_category('Tablets')
# add_category('earphones')
# add_category('Smartphones')

def add_product(name, price, category_name):
    category_name = category_name.lower().strip()
    try:
        category = Category.get(title = category_name)
        print(category, category.title, category.create_at, '!!!!!')
    except peewee.DoesNotExist:
        print(f'Категории {category_name} не существует!')
    else:
        obj = Product(title = name, price = price, category_id = category)
        obj.save()
        print(f'Сохранили товар {obj} - {obj.title}')


add_product('Sony Playstations 5', 700, 'Sony Playstations')
add_product('Sony Playstations 4', 400, 'Sony Playstations')
add_product('Sony Playstations 3', 200, 'Sony Playstations')
