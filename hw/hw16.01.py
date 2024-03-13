"""
1) Создайте словарь тремя возможными способами.
"""
# писать код здесь
# # 1
# this_dict = {
#     'brand': 'Toyota',
#     'model': 'Camri',
#     'year' : 2018
# }
# ls = ['Toyota', 'Camri', 2018]
# print(this_dict, type(this_dict))
# print(this_dict['brand'], this_dict['model'], this_dict['year'])

# # 2
# this_dict = {1: 'keys1', 2: 'keys2', 3: 'keys3' }
# print(this_dict)

# # 3
# this_dict = {}
# this_dict['keys1'] = 'значение 1'
# this_dict['keys2'] = 'значение 2'
# this_dict['keys3'] = 'значение 3'
# print(this_dict)

"""
2) Объявите словарь, удалите один из элементов и распечатайте удалённый элемент.
"""
# писать код здесь

# dict_ = {'name': 'John', 'last_name': 'Snow', 'age': 24}
# print(dict_)
# removed = dict_.pop('last_name')
# print(removed)

"""
3) Объявите словарь, добавьте в него новую пару - "ключ: значение" и распечатайте.
"""
# писать код здесь

# dict_ = {1: 'знач1', 2: 'знач2', 3: 'знач3'}
# print(dict_.setdefault(4, 'ключ: значение'))
# print(dict_)

"""
4) Объявите словарь, удалите всего его элементы и распечатайте.
"""
# писать код здесь
# dict_ = {'name': 'John', 'last_name': 'Snow', 'age': 24}
# print(dict_)
# removed1 = dict_.pop('name')
# removed2 = dict_.pop('last_name')
# removed3 = dict_.pop('age')
# print(dict_)

"""
5) Дан словарь, выведите все его ключи.
"""
# писать код здесь
# this_dict = {
#     'brand': 'Toyota',
#     'model': 'Camri',
#     'year' : 2018
# }
# ls = list(this_dict.keys())
# print(ls)

"""
6)  Объявите словарь, сделайте его копию и распечатайте 
"""
# писать код здесь
# import copy
# this_dict = {1: 'keys1', 2: 'keys2', 3: 'keys3' }
# a = copy.copy(this_dict)
# print(this_dict,a)

"""
7) Это меню вашего ресторана (ключ -- название блюда, значение -- стоимость):
• menu = {'Pad Thai': 200, 'Tom Yam': 170, 'Chicken Teriyaki': 250}
• Добавьте в меню новое блюдо 'Fried Rice' и установите стоимость 150
• Вы решили, что 'Tom Yam' слишком дешевый. Установите новую цену для него: 195
• Ваш повар отвратительно готовит 'Pad Thai', поэтому хотите удалить это блюдо.
• Самостоятельно найдите оператор, который удаляет пару “ключ”:”значение”, и удалите 'Pad Thai' из меню.
• Выведите оставшиеся блюда
"""
# писать код здесь
# menu = {'Pad Thai': 200, 'Tom Yam': 170, 'Chicken Teriyaki': 250}
# menu.setdefault('Fried Rice', 150)
# menu.update({'Tom Yam': 195})
# menu.pop('Pad Thai')
# print(menu)

"""
8) Дан словарь, состоящий из элементов типа: слово-синоним. Все слова в словаре различны. Выведите синоним для последнего слова.
Пример : {‘hello’: ‘hi’, ‘good’: ‘nice’, ‘price’: ‘cost’} --> cost
"""
# писать код здесь
# sinonim = {'hello': 'hi', 'good': 'nice', 'price': 'cost'}
# for value in sinonim.values():
#     pass
# print(value)



"""
9) Создайте три словаря где будут собраны характеристики некоторых животных, затем выведите краткое описание животных.
Пример : dog = {‘name’: ‘Lucky’, ‘age’: 5, 'eyes': 'blue' } --> This is a dog. His name is Lucky. It has blue eyes. Lucky is 2 years old. 
"""
# писать код здесь
# dog = {'name': 'dog', 'name1': 'Lucky','age': 5, 'eyes': 'blue'}
# print(f'This is a {dog["name"]}. His name is {dog["name"]}. It has {dog["eyes"]}. Lucky is {dog["age"]} years old.')
# cat = { 'name': 'cat', 'name1': 'Carnage','age': 3, 'eyes': 'green'}
# print(f'This is a {cat["name"]}. His name is {cat["name"]}. It has {cat["eyes"]}. Lucky is {cat["age"]} years old.')
# trex = { 'name': 'tyrannosaurus', 'name1': 'Rex','age': 70_000_000, 'eyes': 'red'}
# print(f'This is a {trex["name"]}. His name is {trex["name"]}. It has {trex["eyes"]}. Lucky is {trex["age"]} years old.')

"""
10) Создайте словарь в котором будет содержаться информация о факультетах и учениках, ключом будет факультет, а значением список с несколькими учениками. 
Используйте одно имя из списка, который является значением у словаря, для выведения утверждения об этом ученике.
Пример : {'Civil Engineering': ['Thomas', 'Benjamin', 'Franklin'], 'Psycology': ['Joe', 'Chedwick', 'Helena']}
--> This is Franklin. He studies Civil Engineering. 
"""
# писать код здесь
# colleg = {'Civil Engineering': ['Thomas', 'Benjamin', 'Franklin'], 'Psycology': ['Joe', 'Chedwick', 'Helena']}
# a = colleg['Civil Engineering'][1]
# print(f'This is {a}. He studies Civil Engineering. ')

"""
1) Создайте список изпользуя циклы.
"""
# писать код здесь
# dict_ = []
# for x in range(1, 10):
#     dict_.append(x)
# print(dict_)

"""
2) Дан список из чисел, запишите чётные числа в один лист а нечётные в другой лист и выведите результат.
"""
# писать код здесь
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# number1 = []
# number2 = []
# for num in numbers:
#     if num % 2 == 0:
#         number1.append(num)
#     else:
#         number2.append(num)
# print(f"Четные: {number1}")
# print(f"Нечетные: {number2}")

"""
3) Напишите программу, которая найдет факториал введенного числа.
"""
# писать код здесь
# n = int(input('Введите число:'))
# factorial = 1
# for i in range(2, n+1):
#     factorial *= i
# print(factorial)

"""
4) Напишите программу, которая будет находить наибольшую цифру натурального
числа. Натуральное число вводится с клавиатуры. Найти его наибольшую цифру.

"""
# писать код здесь
# number = int(input('Введите натуральное число: '))
# number = str(number)
# number = sorted(number)[::-1]
# number2 = ''
# for i in number:
#     number2 +=i
# number2 = int(number2)
# print(number2)

"""
5) Вам дан список из чисел. Напишите программу в котором вам необходимо найти факториал каждого
числа и записать в новый список.
"""
# писать код здесь
# sp1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sp2 = []
# for i in sp1:
#     fac = i
#     i = 1
#     c = 1
#     while i < fac + 1:
#         c = c * i
#         i += 1

#     sp2.append(c)
# print(sp2) 

"""
6) Вам дан список из чисел. Напишите скрипт в котором она запишет в новый список.
"""
# писать код здесь
# import copy
# sp1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a = copy.copy(sp1)
# print(sp1,a)

"""
7) Создайте пустой список. Напишите программу которая должна 
записывать в ваш список числа от 0 до 10 включительно.
"""
# писать код здесь
# sp1 = []
# for x in range(0, 11):
#     sp1.append(x)
# print(sp1)

"""
8) Вам дан список целых чисел. Напишите программу
которая выводит все элементы которые меньше 7.
"""
# писать код здесь
# sp1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sp2 = []
# for x in sp1:
#     if x > 7:
#         sp2.append(x)
# print(sp2)












