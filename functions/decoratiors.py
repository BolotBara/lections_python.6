# Декораторы - это функция, которая позволяет без изменения кода функции расширить её функционал.

# import requests

# api_url = 'https://api.api-ninjas.com/v1/cars'

# def printCars():
#     car = input('Enter car model: ')
#     api_url = f'https://api.api-ninjas.com/v1/cars?model={car}'
#     response = requests.get(api_url, headers={'X-Api-Key': 'fMvF8LTzSEKonJ8R7LWhEw==GYSkLGG2n8xytyiF'})
#     if response.status_code == 200:
#         print(response.text)
#     else:
#         print(f'ERROR: {response.status_code}\n{response.text}')

# printCars()

# def printUser():
#     api_url = f'https://randomuser.me/api/'
#     response = requests.get(api_url)
#     if response.status_code == 200:
#         print(response.text)

# printUser()

# Заядлый турист ведет тщательный учет своих походов. Во время последнего похода, который занял ровно шаги, за каждым шагом отмечалось, был ли это подъем в гору ,, или спуск ,шаг. Походы всегда начинаются и заканчиваются на уровне моря, и каждый шаг вверх или вниз представляет собойизменение единицы высоты. Мы определяем следующие термины:
# Гора – это последовательность последовательных ступенек над уровнем моря, начиная со ступеньки вверх от уровня моря и заканчивая ступенькой вниз до уровня моря.
# Долина — это последовательность последовательных ступеней ниже уровня моря, начиная со ступеньки вниз от уровня моря и заканчивая ступенькой вверх до уровня моря.
# Зная последовательность подъемов и спусков во время похода, найдите и выведите количество пройденных долин .
# пример 1:
#  path = 8
#  steps = 'UDDDUDUU'
#  result = 1 dolina
# пример 2:
#  path = 10
#  steps = 'DUDDDUUDUU'
#  result = 2 dolina

# steps = 'UDDDUDUU'
# sea_level = 0
# dolina = 0
# for step in steps:
#     if step =='U':
#         sea_level +=1
#         if sea_level == 0:
#             dolina +=1
#     else:
#         sea_level -= 1

# print(f'{dolina}, Dolina')

# Декоратор - это функция, которая позволяет без изменения кода функции расширить функционал этой функции.
# API (Application Programming Interface)

# Функция высшего порядка - это функция кторая принимает другую функцию. Например: декоратор.

# import requests
# from time import time

# def timeCheck(func):
#     def wrapper():
#         start = time()
#         func()
#         finish = time()
#         print(f'Time to get result: {round(finish - start, 2)}')
#     return wrapper

# @timeCheck # -> обязательно начинать с собачкой, it's wrapped
# def printCars():
#     car = input('Enter a car model: ')
#     api_url = f'https://api.api-ninjas.com/v1/cars?model={car}'
#     response = requests.get(api_url, headers={'X-Api-Key': 'fMvF8LTzSEKonJ8R7LWhEw==GYSkLGG2n8xytyiF'})
#     if response.status_code == 200: #-> код для быстрой проверки. существует множество кодов.
#         print(response.text)
#     else: 
#         print(f'Error: {response.status_code}\n{response.text}')
#     return

# @timeCheck
# def printUser():
#     api_url = 'https://randomuser.me/api/'
#     response = requests.get(api_url)
#     if response.status_code == 200:
#         print(response.text)
#     else: 
#         print(f'Error: {response.status_code}\n{response.text}')
#     return

# # printUser()

# printCars()
# print()
# print()
# printUser()

# def decorator(func):
#     def wrapper():
#         print('decorator worked!')
#         print(f'{func.name} была вызванана!')
#         print() #-> just to get otstup
#         func()
#     return wrapper

# @decorator
# def get_name():
#     print(f'Owner name is John Snow!')
# get_name()

# def trace(func):
#     def wrapper(*args, **kwargs):
#         print(f'Tace: вызвала{func._name_}()\ пока приняла args:{args}, kwargs: {kwargs}')
#         res = func(*args, **kwargs)
#         print(f'Tace: вызвала{func._name_}()\ пока вернула: {res}')
#         return res
#     return wrapper

# @trace
# def getAddress(name, adress):
#     return f'Name: {name} -> Address:{adress}'

# @trace
# def getHello(name, last_name, country):
#     return f'Hello {name} {last_name} from {country}'

# print(getAddress('Din Winchester', 'Kansas'))
# print()
# print(getHello('Sam', last_name='Winchester', country= 'Kansas'))

# def boldText(func):
#     def wrapper(*args, **kwargs):
#         res = '<bold>' + func(*args, **kwargs) + '<bold>'
#         return res
#     return wrapper

# def iText(func):
#     def wrapper(*args, **kwargs):
#         res = '<i>' + func(*args, **kwargs) + '<i>'
#         return res
#     return wrapper


# @iText
# @boldText
# def get_name():
#     name = input('Vvedite svoye imya:')
#     return name

# print(get_name())

