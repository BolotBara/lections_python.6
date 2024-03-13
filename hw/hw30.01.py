"""
1) Напишите функцию -- чат-бот, который 
Всегда отвечает “Конечно!” на любой вопрос
Всегда отвечает “Успокойся”, если ты кричишь на него ВОТ ТАК!
Всегда отвечает “Как классно, когда ты молчишь. Продолжай в том же духе!” Если вызвал функцию, но ничего не передал.
В любых других случаях, отвечает “ну и что”
"""

# def chat_bot(user_input: str = None) -> str:
#     if user_input.isupper() and user_input:
#         return 'Успакойся!'
#     elif user_input == ' ':
#         return 'Как классно, когда ты молчишь. Продолжай в том же духе!'
#     elif user_input.endswith('?'):
#         return 'Конечно!'   
#     else:
#         return 'Ну и что'
# while True:
#     print(chat_bot(a:= input('отправьте сообщение боту:')))
#     if a == 'q':
#         break

"""
2) Напишите функцию, которая принимает слово и возвращает True, если слово изограмма (т.е. все буквы в слове уникальны). Иначе возвращает False
"""

# def izogramma(word: str) -> bool:
#     uniq_chars = set(word.lower())  
#     return len(uniq_chars) == len(word)
# word = input("Введите слово: ")
# print(izogramma(word))

"""
3) Подсчет букв:
Напишите функцию, которая принимает строку и возвращает словарь, в котором ключами являются буквы, а значениями — количество их вхождений в строку. Регистр букв не должен учитываться.
"""

# def alpha_stroka(some_str: list) -> dict:
#     alpha = dict()
#     for i in set(some_str):
#         alpha[i] = some_str.count(i)
#     return alpha
# print(alpha_stroka('slovaaaaa'))

"""
4) Поиск подстроки:
Напишите функцию, которая принимает две строки и возвращает True, если вторая строка является подстрокой первой.
"""

# def podstroka(first_str: str= 'hello', second_str: str = 'i' ):
#     if second_str in first_str:
#         return True
#     else:
#         return False
# print(podstroka())
# print(podstroka('hell', 'h'))

"""
5) Напишите функцию, которая проверяет, сколько раз каждое слово в переданной фразе было использовано. Например: “Money, money, money, it’s always sunny, in the richmen’s world”. money: 3, it’s: 1, always: 1, sunny: 1, in: 1, the: 1, richmen’s: 1, world: 1.
"""

# def alpha_stroka(some_str: list) -> dict:
#     alpha = dict()
#     for i in set(some_str.lower().split()):
#         alpha[i] = some_str.lower().count(i)
#     return alpha
# print(alpha_stroka('Money, money, money, it’s always sunny, in the richmen’s world'))

"""
6) Напишите функцию, которая принимает строку и выводит количество гласных, согласных букв и остальных символов. Используйте только кириллические символы
"""

# def stroka(some_str: str) -> dict:
#     sogl = 'qwrtpsdfghjklzxcvbnm'
#     glas = 'eyuioa'
#     alpha = dict()
#     gl = 0
#     sg = 0
#     for i in set(some_str.lower()):
#         if i not in sogl and i not in glas:
#             alpha[i] = some_str.lower().count(i)
#     for x in some_str:
#         if x in sogl:
#             sg += 1
#         else:
#             gl += 1
#     alpha['soglasnye'] = sg
#     alpha['glasnye'] = gl
#     return alpha
# print(stroka('expfpefmeomg!!@$$%'))

"""
7) Вам дан список из нескольких имён в нижнем регистре. Напишите функцию которая записывает начинает первую букву имени в верхнем регистре и сохраните в новом списке.
"""

# def capitalize_names(names):
#     capitalized_names = [name.capitalize() for name in names]
#     return capitalized_names
# names_list = ["anna", "bob", "claire"]
# result = capitalize_names(names_list)
# print(result)

"""
8) Вам дан список из целых чисел. Напишите функцию, в которой Вам необходимо найти факториал каждого из чисел и записать в новый список.
"""

# def factorial(list_: list)-> dict:
#     fack_dict = dict()
#     for i in list_:
#         some_plus = 1
#         for x in range(1,i):
#             some_plus *= x
#         fack_dict[i] = some_plus
#     return fack_dict
# print(factorial([1,2,3,4,5,6,7]))

"""
9) Вам дан список из чисел. Напишите функцию, которая вернёт новый список из квадратов этих чисел.
"""

# def factorial(list_: list)-> dict:
#     fack_dict = dict()
#     for i in list_:
#         fack_dict[i] = i**2
#     return fack_dict
# print(factorial([1,2,3,4,5,6,7]))

"""
10) Напишите функцию average, которая принимает список чисел и возвращает их среднее значение, НЕ используя встроенные функции sum и len
"""

# def average(list_: list) -> int:
#     count = 0
#     len_ = 0
#     for i in list_:
#         count += i
#         len_ += 1
#     return count / len_
# print(average([1,2,3,4,90,6,7,8]))
