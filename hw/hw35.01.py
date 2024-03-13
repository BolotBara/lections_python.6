# 1) '''Магическими называются даты, в которых произведение дня и месяца
# составляет последние две цифры года. Например, 10 июня 1960 года –
# магическая дата, поскольку 10 ´ 6 = 60. Напишите функцию, определя-
# ющую, является ли введенная дата магической. Используйте написан-
# ную функцию в главной программе для отображения всех магических
# дат в XX ве­ке.'''

# def magical_number(day = input('Enter a day: '), month = input('Enter a month in digits: '), year = input('Enter a year: ')):
#     return ('magical number' if int(day) * int(month) == int(str(year)[2:]) else 'No magic in this numbers. ')
# print(magical_number())

# 2) '''Напишите функцию для определения количества дней в конкретном ме-
# сяце. Ваша функция должна принимать два параметра: номер месяца
# в виде целого числа в диапазоне от 1 до 12 и год, состоящий из четырех
# цифр. Убедитесь, что функция корректно обрабатывает февраль високос-
# ного года. В основной программе запросите у пользователя номер месяца
# и год и отобразите на экране количество дней в указанном месяце.'''

# def data(a = int(input('Введите номер месяца в виде целого числа в диапазоне от 1 до 12: ')), \
#          b = int(input('Введите год, состоящий из четырех цифр: '))):
#     ls1 = [1, 3, 5, 7, 8, 10, 12]
#     if a == 2 :
#         if b % 100 ==0: 
#             print('28 дней')
#         else:
#             print('29 дней')
#     elif a != 2:
#         if a == ls1:
#             print('31 день')
#         else:
#             print('30 дней')
# print(data())


# 3) '''Напишите две функции с именами hex2int и int2hex для конвертации
# значений из шестнадцатеричной системы счисления (0, 1, 2, 3, 4, 5, 6, 7,
# 8, 9, A, B, C, D, E и F) в десятичную (по основанию 10) и обратно. Функ-
# ция hex2int должна принимать на вход строку с единственным символом
# в шестнадцатеричной системе и преобразовывать его в число от нуля
# до 15 в десятичной системе, тогда как функция int2hex будет выполнять
# обратное действие – принимать десятичное число из диапазона от 0 до
# 15 и возвращать шестнадцатеричный эквивалент. Обе функции должны
# принимать единственный параметр со входным значением и возвращать
# преобразованное число. Удостоверьтесь, что функция hex2int корректно
# обрабатывает буквы в верхнем и нижнем регистрах. Если введенное поль-
# зователем значение выходит за допустимые границы, вы должны вывести
# сообщение об ошибке.'''

# def hex2int(a):
#     try:
#         return int(a, 16)
#     except ValueError:
#         print("Ошибка: Введенное значение не является допустимым символом шестнадцатеричной системы.")
#         return None

# def int2hex(b):
#     if 0 <= b <= 15:
#         return hex(b)[2:].upper()
#     else:
#         print("Ошибка: Введенное число должно быть в диапазоне от 0 до 15.")
#         return None
# print(hex2int('1')) 
# print(int2hex(12))

# 4) '''Представьте, что в вашем регионе устаревшим является формат номер-
# ных автомобильных знаков из трех букв, следом за которыми идут три
# цифры. Когда все номера такого шаблона закончились, было решено об-
# новить формат, поставив в начало четыре цифры, а за ними три буквы.
# Напишите функцию, которая будет генерировать случайный номерной
# знак. При этом номера в старом и новом форматах должны создаваться
# примерно с одинаковой вероятностью. В основной программе нужно сге-
# нерировать и вывести на экран случайный номерной знак.'''

# from string import ascii_letters, digits
# from random import choices

# def decor(func):
#     def wrapper(*args, **kwargs):
#         old_number = ''.join(choices(ascii_letters, k=3))+ ''.join(choices(digits, k=3))
#         new_number = ''.join(choices(digits, k=4))+ old_number[:3]
#         print(f'old number: {old_number}')
#         print(f'new number: {new_number}')
#     return wrapper

# @decor
# def func(old, new):
#     return 'old_number, new_number'
# func(34, 56)
