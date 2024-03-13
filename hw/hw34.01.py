# 1) Создайте функцию, которая генерирует рандомное (случайно сгенерированное) число и выводит на окно терминала через команду print(). Далее создайте декоратор, который журналирует это событие. То есть функция декоратор должна писать в dict() предложение: «Функция …………… была запущена успешно», а ключом будет уникальный идентификатор (id).   (15 баллов)

# from random import randint

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print(f"Функция {func.__name__} была запущена успешно")
#         return result
#     return wrapper

# def chislo():
#     a = randint(1,10)
#     print(a)
# chislo()


# 2) Напишите функцию, которая принимает фразу, и возвращает его сокращенную форму.
# Например: Кыргызская Республика -- КР. Ruby on Rails -- ROR. For your interest -- FYI и т.п. (10 баллов)

# def pop(puk = input('Введите предложение: ')):
#     a = puk.split() 
#     b = ''.join(x[0].upper() for x in a)
#     return b
# print(pop())

# 3) '''Напишите декоратор, который проверяет, что функция вызывается с определенными типами аргументов.''' (15 баллов)

# def dicobraz(*types):
#     def decorator(func):
#         def wrapper(*args, **qwargs):
#             for i, arg in enumerate(args):
#                 if not isinstance(arg, types[i]):
#                     raise TypeError(f"Аргумент {i+1} должен быть типа {types[i].__name__}")
#             return func(*args, **qwargs)
#         return wrapper
#     return decorator

# @dicobraz(int, str)
# def example_func(num, text):
#     print(f"Вызвана функция с аргументами: {num}, {text}")

# example_func(10, "hello")  
# example_func("world", 5)   


# 4) '''Создайте декоратор, который автоматически преобразует результат функции в другой тип данных,''' (15 баллов)

# def decor(func):
#     def wrapper(*args, **gwargs):
#         print(type(func(*args, **gwargs)))
#         a = str(func(*args, **gwargs))
#         print(type(a))
#         return a
#     return wrapper
# @decor
# def sum(a,b):
#     return a + b
# print(sum(3, 4))


# 5) '''Реализуйте декоратор, который ограничивает максимальное количество вызовов функции.''' (20 баллов)

# def decorator(func):
#     def wrapper(*args):
#         attempts = 10
#         while attempts:
#             print(f'длина: {func(input("Введите что-нибудь: "))}')
#             print(f'{attempts} попыток осталось')
#             attempts -= 1
#     return wrapper

# @decorator
# def bonc(a):
#     return len(a)
# print(bonc())


# 6) '''Напишите декоратор, который автоматически логирует исключения, возникающие внутри функции.''' (15 баллов)

# def decorator(func):
#     def wrapper(*args, **qwargs):
#         try:
#             return func(*args, **qwargs)
#         except Exception as e:
#             print(f"Возникло исключение в функции {func.__name__}: {e}")
#             raise
#     return wrapper

# @decorator
# def bonc(a, b):
#     return a * b

# print(bonc(2, 2))         


# 7) '''Напишите декоратор, который ограничивает доступ к функции только определенным пользователям или ролям.''' (15 баллов)

# def ogr(allowed_users):
#     def decorator(func):
#         def wrapper(user, *args, **qwargs):
#             users_ = allowed_users.get(user, [])
#             if 'admin'in users_ or user in users_:
#                 return func(*args, **qwargs)
#             else:
#                 raise PermissionError('Доступ запрещён')
#         return wrapper
#     return decorator

# users_ = {
#     'Itodori': ['role1'],
#     'Maki': ['role2'],
#     'Todji': ['admin']
# }

# @ogr(users_)
# def fun(*args, **qwargs):
#     print("Функция доступна только определенным пользователям или ролям")

# print(fun('Todji'))
