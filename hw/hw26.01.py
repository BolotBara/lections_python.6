"""
Задания по исключениям.
"""
"""
1) Опишите полный синтаксис конструкции try-except:
"""
# писать код здесь
# try:
    # <body>
# except:
    # <body except> 
    # print()

"""
2) Дан следующий код:
b = 10
c = 11
print(a)
Обработайте ошибку, которая может возникнуть.
"""
# писать код здесь

# b = 10
# c = 11
# try:
#     print(a)
# except NameError:
#     print('Нет такой переменной')

"""
3) Напишите программу которая будет получать два числа через input и делить одно на другое. Обработайте ошибку, которая возникнет в случае, если второе число окажется 0 и выведите сообщение.
"""
# писать код здесь

# try:
#     num1 = int(input('Enter the number1: '))
#     num2 = int(input('Enter the number2: '))
#     print(f'{num1} / {num2} = {num1 / num2}')
# except:
#     print('Invelid Values!')

"""
4) Напишите программу, которая будет получать через инпут 2 числа и будет печатать их сумму. Обработайте ошибку, которая возникнет, если пользователь введёт не числовое значение и выведите сообщение.
"""
# писать код здесь

# try:
#     num1 = int(input('Enter the number1: '))
#     num2 = int(input('Enter the number2: '))
#     print(f'{num1} + {num2} = {num1 + num2}')
# except ValueError:
#     print('Ты ввел неправильные данные для функции int имбицыл!')

"""
5) Дан словарь. Попытайтесь получить значение по ключу. Обработайте ошибку, возникающую в том случае, если запрашиваемый ключ не существует.
"""
# писать код здесь

# dict_ = {1: 'one', 2: 'two', 3: 'three'}
# try:
#     key = int(input('Vvedite key: '))
#     print(dict_[key])
# except KeyError:
#     print('Ishak takogo key net, vnimatelno posmotri chto vvodish!' )

"""
6)  Дан список. Обработайте исключение при попытке обращения к несуществующему элементу.
"""
# писать код здесь
# ls = [1, 2, 3, 4, 5]
# try:
#     index = int(input('Vvedite index: '))
#     print(ls[6])
# except IndexError as i:
#         print(i)

"""
7) Попытайтесь в блоке try принять 2 числа и разделить одно на другое. В блоке except обработайте сразу 2 возможных исключения.
"""
# писать код здесь

# try:
#     num1 = int(input('Enter the number1: '))
#     num2 = int(input('Enter the number2: '))
#     print(f'{num1} / {num2} = {num1 / num2}')
# except ValueError:
#     print('Ты ввел неправильные данные для функции int имбицыл!')
# except ZeroDivisionError:
#     print('Ишак на ноль делить нельзя')

"""
😍 Запросите у пользователя сумму, которая у него сейчас есть в бумажнике. Если он введёт сумму, меньшую чем 0, то выбросите исключение с текстом "Сумма не может быть отрицательной!"
"""
# писать код здесь

# num1 = int(input('Введите сумму, которая у вас сейчас есть в бумажнике: '))
# if num1 < 0:
#     raise TypeError('Сумма не может быть отрицательной!')

"""
9)  В блоке try запросите у пользователя ввод его возраста. Затем в том же блоке проверьте его возраст на совершеннолетие. Если пользователь несовершеннолетний, выбросите исключение с текстом "Доступ запрещён". Обработайте также исключение если пользователь вводит текст вместо числа с сообщением 'Введен некорректный возраст'. Если ошибок не возникло, то распечатайте сообщение "Спасибо!", а затем "До свидания", вне зависимости от того, произошла ошибка или нет.
"""
# писать код здесь

# try:
#     age = int(input('Сколько вам лет:'))
#     if age< 18:
#         print('Доступ запрещён!')
#     else:
#         print('Спасибо')
# except ValueError:
#     print('Введен некорректный возраст!')
# print('До свидания!')