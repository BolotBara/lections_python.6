# найти квадрат, куб, результат деления на 100 любых 3 чисел

# num = 5
# {'num': 5. '2': 25, '3': 125, '100': 0.05  }

# num1 = 5
# num2 = 75
# num3 = 1154
# res1 = {'num': num1, '2': num1 ** 2, '3': num1 ** 3, '100': num1 / 100}
# res2 = {'num': num2, '2': num2 ** 2, '3': num2 ** 3, '100': num2 / 100}
# res3 = {'num': num3, '2': num3 ** 2, '3': num3 ** 3, '100': num3 / 100}
# print(res1,res2,res3, sep='\n\n')

# DRY - Don't repeat yourself

# def do_operations(num: int) -> None:
#     res = {'num': num, '2': num ** 2, '3': num ** 3, '100': num / 100}
#     print(res)
# do_operations(5)
# do_operations(75)
# do_operations(1154)
# ----------------------------------------------------------------------------------------
# Функция это именованная часть программы которая содержит в себе определённый блок кода и может вызываться в других частях программы столько раз сколько угодно

# def name_of_func(<a, b> параметры фунции):
    # <body> # код, какая то логика которая будет давать конечный результат
    # <return> # оператор который помогает сохранить результат
#  name_of_func(4, 6 # аргументы)

# параметры функции - переменные в которых мы временно сохраняем данные которые передаем при вызове в функцию, они доступны только внутри функции

# аргументы функции - данные которые мы передаем при вызове функции, они попадают в параметры по очередно

# def isEven(num):
#     return True if num % 2 == 0 else False

# res1 = isEven(16)
# res2 = isEven(17)
# print(res1, res2)

# def isEven(num: int) -> bool:
#     """Return True or False after checking number for even!"""
#     return True if num % 2 == 0 else False

# default параметры
# def sum_of_args(a: int, b: int, c: int=0) -> int:
#     """Returns sum of given arguments"""
#     try:
#         return a + b + c
#     except TypeError:
#         raise Exception('Invalid values for arguments')
    
# print(sum_of_args(1, 2))
# print(sum_of_args(6, 9, 12))
# print(sum_of_args(6, 9, None))

# -----------------------------------------------------------------------------

# print(len('string'))
# from typing import Iterable

# def our_len(obj: Iterable) -> str:
#     """Возвращает длину итерируемого объекта"""
#     i = 0 
#     print(obj)
#     for _ in obj:
#         i += 1
#     print(f'result: {i}')

# our_len([1, 2, 3, 4, 5])
# our_len('string Hello world My name is John Snow')

# -------------------------------------------------------------------------------

# 'Hello World My name is John, last name is Snow. Nice to meet to you! '

# 'you! to meet to Nice Snow. is ...'

# 'hello world snow king'
# 'king snow world hello'

# def reverse_text(text: str) -> str:
#     spisok = text.split()
#     return ' '.join(spisok[::-1])

# str1 = 'Hello World My name is John, last name is Snow. Nice to meet to you!'
# print(reverse_text(str1))
# print(reverse_text('hello world snow king'))

