"""=================EASY=================="""
# # /// TASK1 \\\
# # Дан список целых чисел, найдите минимальное значение, не используя встренную функцию min()
# # Например:
# list_ = [20, 10, 20, 1, 100]
# # Результат:
# min_number = list_[0]
# for i in list_:
#     if i < min_number :
#         min_number = i
# print('min_number =', min_number)
        
# # /// TASK2 \\\
# # Дан список с кортежами, выведите список без пустых кортежей
# # Например:
# tuples = [(), ('ram','15','8'), (), ('laxman', 'sita')]
# # Результат:
# for x in tuples:
#     if x == ():
#         tuples.remove(x)
# print(tuples)

# # /// TASK3 \\\
# # Запросите у пользователей 5 раз их имя и фамилию, но в списке сохраните лишь фамилию, также учтите, что
# # у человека ФИО может состоять не только из 2 слов. При выводе должен выходить отсортированный
# # в алфавитном порядке список

# # Наример:
# # Name: Maya Angelou
# # Name: Chimamanda Ngozi Adichie
# # Name: Tobias Wolff
# # Name: Sherman Alexie
# # Name: Jane Austen
# # Результат:
# user = []
# i = 5
# while i > 0:
#     if i > 0 :
#         name = input('Введите имя и Фамилию: ').split()
#         user1 = name[1]
#         i -= 1
#         user.append(user1)
# user.sort()
# print(user)

# # /// TASK4 \\\
# # Вам дан список из чисел, и переменная x в которой хранится число, 
# # посчитайте сколько вхождений этого числа в этом списке 

# # Например:
# list_ = [8, 6, 8, 10, 8, 20, 10, 8, 8]
# x = 8
# # Результат:
# count_x = list_.count(x)
# print(count_x)

# # /// TASK5 \\\
# # Вам дан список с числами и строками, найдите сумму чисел в этом списке не используя функцию sum()
# # Например:
# lists = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# # Результат:
# a = 0
# for x in lists:
#     if type(x) == int:
#         a += x
# print(a)

# # /// TASK6 \\\
# # Вам дан список из строк, в которых длина строки равна 2 или более, в новый список запишите индексы тех строк, у которых
# # первый и последний символы совпадают.
# # Например:
# str_list = ['abc', 'xyz', 'aba', '1221']
# # Результат:
# indices = [i for i, s in enumerate(str_list) if len(s) >= 2 and s[0] == s[-1]]
# print(indices)

# # /// TASK7 \\\
# # У вас есть список со вложенными списками, выведите самый длинный список и самый короткий
# # Например:
# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# # Результат:
# max_list = max(lists, key=len)
# min_list = min(lists, key=len)
# print("max_list", max_list, "min_list", min_list)

# # /// TASK8 \\\
# # Вам дан список, напишите код, который будет соединять в новый список элементы по n-ному шагу
# # Например:
# n = 3
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# #  Результат:
# result = [list_[i::n] for i in range(n)]
# print(result)

# # /// TASK9 \\\
# # Напишите код для создания матрицы с размером 3x3
# # Результат:
# matrix = [[1, 2, 3] for _ in range(3)]
# print(matrix)

# /// TASK10 \\\
# Вам дан список со словами, пользователь вводит первую букву слова, которое он ищет,
# ваш код должен вывести список со всеми словами, начинающимися на эту букву
# Например:
# list_ = ['sun', 'flowers', 'rumor', 'stranger', 'adventure', 'architect', 'accompany', 'abandon', 'cartoon']
# letter = input("Найди мне слово начинающееся на букву: ")
# filtered_list = [word for word in list_ if word.startswith(letter)]
# print(filtered_list)

"""=====================MEDIUM========================"""

# /// TASK1 \\\
# Вам даны 2 списка, напишите код, который будет выводить разницу первого списка от второго и наоборот
# Например:
# color1 = ["red", "orange", "green", "blue", "white"]
# color2 = ["black", "yellow", "green", "blue"]
# diff_color1_color2 = list(set(color1) - set(color2))
# diff_color2_color1 = list(set(color2) - set(color1))
# print("Color1-Color2:", diff_color1_color2)     
# print("Color2-Color1:", diff_color2_color1)

# /// TASK2 \\\
# Вам даны 2 списка из чисел, нужно написать код, который будет выводить True,
# если есть хотя бы один общий элемент, в ином случае False
# Например:
# list1 = [1, 2, 3, 4, 5]
# list2 = [5, 6, 7, 8, 9]
# has_common_element = any(element in list2 for element in list1)
# print(has_common_element)

# /// TASK3 \\\
# Вам дан список, выведите числа, частота повторений которых больше или равно K
# Например:
# list_ = [4, 6, 4, 3, 3, 8, 4, 3, 4, 3, 8, 8]
# K = 2
# counter_dict = {}
# for num in list_:
#     counter_dict[num] = counter_dict.get(num, 0) + 1
# result = [num for num, count in counter_dict.items() if
#     count >= K]
# print(result)

# /// TASK4 \\\
# Вам дан список из 3 чисел, выведите все возможные комбинации с этими числами
# Например:
# list_ = [1, 2, 3]
# combinations = [[a, b, c] for a in list_ for b in list_ for c in list_]
# for combination in combinations:
#     print(*combination)

# /// TASK5 \\\
# Создайте список с 3 вложенными списками списками, где внутри должно быть три 0
# Результат:
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# matrix_zeros = [[0, 0, 0] for _ in range(3)]
# print(matrix_zeros)

# /// TASK6 \\\
# Вам дан список со строками, необходимо перевернуть эти строки, а также отсортировать по длине
# Например:
# colors = ["Red", "Green", "Blue", "White", "Black", "Yellow", "Orange"]
# reversed_sorted_colors = sorted([color[::-1] for color in colors], key=len)
# print(reversed_sorted_colors)

# /// TASK 7 \\\
# Вам дан список с элементами, добавьте элемент, который хранится в переменной x в этот список после каждого n-ого шага
# Например:
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# n = 2
# x = 'a'
# for i in range(1, len(nums) // n + 1):
#     nums.insert(i * n + (i - 1), x)
# print(nums)

"""=================HARD===================="""

# /// TASK1 \\\
# Вам дан список со вложенными списками, выведите тот список, у которого самая большая сумма
# Например:
# lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
# max_sum_list = max(lists, key=sum)
# print(max_sum_list)

# /// TASK2 \\\
# Дан список целых чисел с повторяющимися элементами. Вам надо создать еще один список, содержащий только
# повторяющиеся элементы. Проще говоря, новый список должен содержать элементы, которых больше одного.
# Например:
# list_ = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# repeated = [item for item in set(list_) if list_.count(item) > 1]
# print(repeated)

# /// TASK3 \\\
# Вам дан список из букв, пользователь вводит 2 буквы, от какой и до какой буквы нужно соединить в одну строку,
# ваш код должен соединить эти буквы
# Например:
# chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# start_char = input("От какой: ")
# end_char = input("До какой: ")
# merged_string = ''.join(chars[chars.index(start_char): chars.index(end_char) + 1])
# print(merged_string)




