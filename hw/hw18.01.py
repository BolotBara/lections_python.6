# 1) Пользователи банкомата хотят снимать деньги. Но банкомат выдаёт только купюры по 100
# рублей. Напишите программу, которая проверяет допустимость денежной суммы, которую ввёл пользователь.
# Пример:

# Введите сумму которую хотите снять: 250
# Такую сумму снять невозможно, обратитесь в другой банкомат
# """

# money = int(input("Введите сумму, которую хотите снять: "))

# if money % 100 != 0:
#     print('Банкомат выдаёт только купюры по 100 сом. Чтобы снять полную сумму обратитесь в другой банкомат.')
# if money % 100 == 0:
#     print('Перед тем, как уйти посчитайся ваши деньги!')

""" 2)'''Назовем число красивым, если оно является четырехзначным и делится нацело на 7 или на 17. Напишите программу, определяющую, является ли введённое число красивым. Программа должна вывести «YES», если число является красивым, или «NO» в противном случае.
Формат входных данных
На вход программе подаётся натуральное число.
Формат выходных данных
Программ

"""
# num = int(input('Enter a number (****), if you want to check, if it\'s beautiful: '))
# if num not in range(1000, 10000):
#     raise ValueError('A number is not more than 10000 or less than 1000')
# while num in range(1000, 10000):
#     if num % 7 == 0 or num % 17 == 0:
#         print('Yes')
#         break
#     else:
#         print('No')
#         break

"""
3) Мурат с друзьями на выходных решил собраться и пойти в ночной клуб.
Но в ночной клуб пропускают только тех, кому 17+.
Мурату - 24 года, Эржану - 21 год, Карине - 24 года, Алтынай - 17 лет, Айбеку - 16 лет.
Напишите программу, которая определяет кого пустить в ночной клуб, а кого нет. (работа со словарем)
"""
# dict = {
#     'Мурат': 24, 'Эржан': 21, 'Каринa': 24, 'Алтынай': 17, 'Айбек': 16
# }

# 


"""
4) Задание 
Запросите у пользователя число от 1 до 10 в переменную n. Затем пройдитесь по промежутку чисел от 1 до 500(включительно) 
и запишите в словарь dict_, только те числа, которые кратны числу n (делятся на число n без остатка), введенное пользователем. 
Ключом будет само число, а значением его квадрат.
"""
# n = int(input('Введите число от 1 до 10: '))

# dict_ = {}
# for i in range(1, 501):
#     if i % n == 0:
#         dict_.update({i: i **2})
# print(dict_)


"""
5) Дан словарь, в котором ключом является имя студента, а значением словарь с его оценками по 3 предметам. 
Замените оценки названием предмета, по которому студент имеет высший балл. 
Например: a = {'John': {'history': 90, 'math': 95, 'literature': 91}, 'Rose': {'history': 92, 'math': 96, 'literature': 81}, 'Kelly': {'history': 84, 'math': 85, 'literature': 87}}
-Результат: {'John': 'math', 'Rose': 'math', 'Kelly': 'literature'}
"""
# a = {
#     'John': {'history': 90, 'math': 95, 'literature': 91}, 
#     'Rose': {'history': 92, 'math': 96, 'literature': 81}, 
#     'Kelly': {'history': 84, 'math': 85, 'literature': 87}
#     }
# a['John'] = max(a['John'], key = a['John'].get)
# a['Rose'] = max(a['Rose'], key = a['Rose'].get)
# a['Kelly'] = max(a['Kelly'], key = a['Kelly'].get)
# print(a)


"""
6) Дан словарь, значениями в котором являются другие словари. Замените внутренние словари их значениями. Например: my_dict = {'first': {'a': 1}, 'second': {'b': 2}}
 -> {'first': 1, 'second': 2}
"""
# my_dict = {
#     'first': {'a': 1}, 
#     'second': {'b': 2}
#     }  

# print(my_dict.update({'first': 1}))




"""
7) У Ирины футболки 2 цветов. Ирина одевает красную футболку в чётные числа месяца, а синюю в нечётные. 
Напишите программу, которая по введённому числу месяца определяет какую футболку нужно одеть Ирине сегодня.
"""

# i = int(input('Vvedite today chislo: '))

# if i > 31:
#         print('This date diesn\'t exist.')
# else:
#     if i % 2 == 0 and i < 32:
#         print('Blue')
#     if i % 2 != 0 and i < 32:
#         print('Red')

"""
8) Вам дан список целых чисел. Напишите программу которая выводит все элементы, которые меньше 7. 
"""

# ls = [89, 98, 21, 17, 33, 6, 3]
# ls1 = []
# for i in ls:
#     if i > 7:
#         ls1.append(i)
# print(ls1)