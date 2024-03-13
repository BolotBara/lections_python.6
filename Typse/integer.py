# Типы данных числа -> int, float 

# = -> оператор присваивания
# num = 5
# print(num) # 5
# num = 79 # переопределение
# print(num) # 79
# num += 1 # num = num + 1
# print(num) # 80
# num -= 5
# print(num)

# abc -> нижний геристр
# ABC -> верхний регист

# PEP8 
# tomorrow_day = '11.01.2024' # Snake case 
# tomorrowDay = '11.01.2024' # Camel case 

#  +
# num1 = 5 
# num2 = 15
# result = num1 + num2
# print(result)

# -
# num1 = int(input('Enter the num1:'))
# num2 = int(input('Enter the num2:'))
# print(num2, '-', num1, '=', num2 - num1)

# *
# num1 = int(input('Enter the num1:'))
# num2 = int(input('Enter the num2:'))
# print(num2, '*', num1, '=', num2 * num1)

# / and // and %
# / - обычное деление
# // - деление без остатка
# % - модульное деление (получение остатка от деления)

# num1 = 8
# num2 = 3
# print('/', num1 / num2)
# print('//', num1 // num2)
# print('%', num1 % num2)

# ** -> возведение в степень

# print(5 ** 2)
# print(17 ** 55 )

# print(144 ** 0.5), print(144 ** (1/2)) # квадратный корень
# print(36 ** 0.5)

# res = 5 * (15 + 5)
# print(res)

# pow - возведение в степень 
# pow(num1, num2, <mod>)
# print(pow(5, 2)) # 5 ** 2
# print(pow(5, 2, 2)) # 5 ** 2 % 2

# a = 6
# c = 3 
# res = pow(a, c, 50)
# print(res)

# abs() - абсолютное значение числа -> abs(-5) -> 5
                                         #(-5) -> 5

# a = abs(-15)
# b = abs(15)
# c = abs(-2.5)
# print(a, b, c)

# round() - округление числа с плавающей точкой
# a = 5.57
# print(round(a))

# b = 7.368232
# print(round(b, 2))

# divmod(a, b)  - она выводит 2 числа, 1 число это результат целого деления(//), а 2 число это модульное деление чисел a и b  

# print(22 / 5) # 4.4
# print(divmod(22 , 5))

# import math

# a = 5
# print(round(math.sqrt(5), 1))

# множественное присваивание
# a = 'moloko'
# b = 'voda'
# c = None
# a, b = b, a
# print(a, b)

# num1, num2, num3 = input('num1: '), input('num2: '), input('num3: ')
# print(num1)
# print(num2)
# print(num3)

# from math import pi

# r = int(input('Vvedite radius: '))
# resP = 2 * r * pi
# resS = r ** 2 * pi
# print('S okruznosti: ', round(resS, 2))
# print('P okruznosti: ', round(resP, 2))

# from random import randint

# num = randint(1, 10)
# print(num)
# i = 0
# while i < 3:
#     quess = int(input('Ugadai chislo: '))
#     if quess == num: 
#         print('YOU WIN!')
#         i = 3
#     i += 1



  











