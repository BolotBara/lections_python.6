# dict() - Словарь - упорядоченная коллекция элементов.(pithon 3.7-> orderet). Каждый элемент внутри словаря хранится в виде пары --> {ключ! значение}
# ассоциативный массив, hash table, object(js), structure == dictionary(py)

# ключамии могут быть только неизмеримые типы данных и в словаре сохраняются только уникальные ключи
# тогда как значениями могут  выступать любые типы данных и любые значения

# thisdict = {
#     'brand': 'Ford',
#     'model': 'Mustang',
#     'year' : 1967
# }
# ls = ['Ford', 'Mustang', 1976]

# print(thisdict, type(thisdict))
# print(thisdict['brand'], thisdict['model'], thisdict['year'])

# thisdict['motor'] = 'GTI Turbo'
# thisdict['model'] = 'fiesta'
# print(thisdict['model'], thisdict['motor'])

# print(dir(dict))
# items, keys, values

# user_info = {
#     'first_name' : 'John',
#     'last_name' : 'Snow',
#     'age' : 24,
#     'email' : 'bastard123@gmail.com',
#     'role' : 'admin',
# }

# print(user_info)

# ls = list(user_info.keys()) - вытаскивает ключ
# print(ls)

# ls2 = list(user_info.values()) - вытаскивает значение 
# print(ls2)

# ls3 = list(user_info.items()) - вытаскивает всё в виде кортежей
# print(ls3)

# print('\nValues:')
# for value in user_info.values():
#     print(value)

# print('\nKeys:')
# for key in user_info.keys():
#     print(key)

# print('\nItems:')
# for key, value in user_info.items():
#     print(f'keys:{key}, values: {value}')


# изменение 
# dict_ = {'name': 'Jack', 'age' : 17}
# print(dict_['name'])
# dict_['name'] = 'john'
# dict_['address'] = 'WinterFell'
# print(dict_)
# dict_.update(age = 24, adddres = 'Blackcastle')
# print(dict_)
# dict_.update({'name': 'John Snow'})
# print(dict_)

# dict_ = {1: 'Pizza', 2: 'Burger', 3: 'Steak'}
# print(dict_[3], '!!!')
# print(dict_.get(3, 'Not Found!'))

# setdefault - работает так же как и get, но если нет такого ключа то создает пару из этого ключа

# dict_ = {1: 'Pizza', 2: 'Burger', 3: 'Steak'}
# print(dict_.setdefault(5, 'Sushi'))
# print(dict_)

# создание - fromkeys
# ls = list(range(1, 20))
# new_dict = dict.fromkeys(ls, 'default')
# print(new_dict)

# удаление элементов
# pop, popiyem

# pop(<key>) - удаляет пару от ключа
# popitem() - удаляет последнюю пару 

# dict_ = {'name': 'John', 'last_name': 'Snow', 'age': 24}
# print(dict_)
# removed = dict_.pop('last_name')
# print(dict_)
# print(removed)
# print('----------------')
# removed = dict_.popitem()
# print(dict_)
# print(removed)

# roles = {
#     1: 'Admin',
#     2: 'Custom',
#     3: 'Vendor',
# }
# users = {
#     55: {
#         'id': 55, 'role': roles[3], 'username': 'Tirion'
#     },
#     12: {
#         'id': 12, 'role': roles[1], 'username': 'John Snow'
#     },
#     4: {
#         'id': 4, 'role': roles[2], 'username': 'Taylor'
#     },
# }
# print(users)

# product = {
#     'id': 1,
#     'title': 'Sumsung Galaxy S23 Ultra',
#     'description': 'Lorem ipsum',
#     'price': 1000
# }
# print(product)

# id_user = int(input('Vvedite id: '))
# if users[id_user] ['role'] == roles[1]:
#     product['description'] = input('Vvedite opisanie: ')
# else:
#     print('You don\'t have permissions!')

# print()
# print(product)

# age = input('Enter your age: ')

# if age.isdigit():
#     age = int(age)
# else:
#     raise Exception('Invalid value for age!')

# if age < 18:
#     print(f'Access denied! come again after {18-age} year')
# else:
#     print('You\'re welcome!')
