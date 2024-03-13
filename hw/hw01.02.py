# 1) Напишите функцию, которая принимает строку и вычисляет количество букв верхнего и нижнего регистра.

# def slova(a):
#     slova_A = 0
#     slova_a = 0
#     for i in a:
#         if i.islower():
#             slova_a +=1
#         else:
#             slova_A +=1
#     return slova_A, slova_a
# print(slova(input('Введите слово: ')))

# 2) Напишите функцию, которая принимает число n и генерирует словарь, чьи ключи состоят из чисел от 1 до n, а их значения -- куб ключей. Пример: передано число 5. В результате должны получить словарь {1: 1, 2: 8, 3: 27, 4: 64}

# def func(n):
#     dict_={}
#     for i in range(1, n+1):
#         dict_[i] = i **3
#     return dict_
# print(func(4))


# 3) Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения «start» до величины «end» включительно. Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.

# def sum_range(start, end):
#     sum_ = 0
#     if start > end:
#         start, end = end, start 
#     for i in range(start, end):
#         sum_ += i
#     return sum_

# print(sum_range(1, 10))
# print(sum_range(100, 10))

