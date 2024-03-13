# Задание 1.

# Есть список list_1 = [5.97, 6, "tom", 3.14, "bob", "alice", 5, -35, "nursultan", 42, "ulukbek", "edil", 91, "nurlan", 1.5, 27.9]
#      Написать функцию которая будет принимать этот список в качестве аргумента. Далее функция должна ВЕРНУТЬ список состоящий из имен(строковых значений) и чтобы эти имена были с заглавной буквы и в алфавитном порядке
#     Написать функцию которая будет принимать этот список в качестве аргумента. Далее функция должна ВЫВЕСТИ НА КОНСОЛЬ список из целочисленных значений в отсортированном виде но в обратном порядке, т.е от большого к маленькому
#     Написать функцию которая будет принимать этот список в качестве аргумента. Далее функция должна ВЕРНУТЬ сложение всех чисел с плавающей точкой

# list_1 = [5.97, 6, "tom", 3.14, "bob", "alice", 5, -35, "nursultan", 42, "ulukbek", "edil", 91, "nurlan", 1.5, 27.9]

# def names_list_sorted(list_1):
#     names = [str(item).capitalize() for item in list_1 if isinstance(item, str)]
#     names.sort()
#     return names

# print(names_list_sorted(list_1))

# def sorted_integers(list_1):
#     integers = [item for item in list_1 if isinstance(item, int)]
#     integers.sort(reverse=True)
#     print(integers)

# sorted_integers(list_1)

# def sum_floats(list_1):
#     float_numbers = [item for item in list_1 if isinstance(item, float)]
#     return sum(float_numbers)

# print(sum_floats(list_1))

# Задание 2.

# Сэндвичи: напишите функцию, которая получает первым аргументом размер сэндвича в виде строкового значения и список компонентов сэндвича.
# При вызове функции, функция должна выводить описание заказанного сэндвича например «Большой сэндвич со следующими ингредиентами: огурец, колбаса … » . Вызовите функцию три раза с разными количествами аргументов и разными размерами (Большой, средний, маленький)

# def candvich(a, b):
#     print(a,'сэндвич со следующими ингредиентами:', b)

# candvich(input('Введите размер сэндвича(Большой, средний, маленький): '), input('Введте компоненты сендвича: '))

# Задание 3.

# Напишите функцию для сохранения информации об автомобиле в словаре . Функция всегда должна возвращать производителя и название модели, но при этом она может получать произвольное количество именованных аргументов . Вызовите функцию с передачей обязательной информации и еще двух пар «имя—значение» (например, цвет и комплектация) . Ваша функция должна работать для вызовов следующего вида: car = make_car(‘subaru’, ‘outback’, colour=’blue’, engine='V8') и возвращать строку" Subaru Outback colour is blue, engine is V8

# def make_car(proizvoditel, model, **kwargs):
#     car_info = proizvoditel.capitalize() + " " + model.capitalize()
#     if kwargs:
#         car_info += ", " + ", ".join([f"{key} is {value}" for key, value in kwargs.items()])
#     return car_info  
# car = make_car('Toyota', 'Kamri', color = 'black', engine = 'V8')
# print(car)

# Задача 4

# Напишите функцию count_letters, которая принимает на вход текст и подсчитывает, какое в нём количество цифр и букв. Функция должна вывести на экран информацию о найденных буквах и цифрах в определённом формате.
# Реализовать в цикле while, для выхода пользователь должен ввести "выход"

# Пример:
# Введите текст: 100 лет в обед
# Какую цифру ищем? 0
# Какую букву ищем? л
# Количество цифр 0: 2
# Количество букв л: 1

# def count_letters(text):
#     digit_count = 0
#     letter_count = 0

#     while True:
#         digit_to_find = input('Какую цифру ищем? (или "q" для завершения): ')
#         if digit_to_find.lower() == 'q':
#             break

#         letter_to_find = input('Какую букву ищем? (или "q" для завершения): ')
#         if letter_to_find.lower() == 'q':
#             break

#         digit_count = text.count(digit_to_find)
#         letter_count = text.count(letter_to_find)

#         print(f"Количество цифр {digit_to_find}: {digit_count}")
#         print(f"Количество букв {letter_to_find}: {letter_count}")
#         break

# text_input = input('Введите текст: ')
# count_letters(text_input)

# Задача 5.

# Напишите функцию, которая в виде аргумента принимает словарь (данные с именами и должностями , где ключ это имя работника,  а значение его должность. Функция должна вернуть предложения, типа:  
# Работник Асан, занимает должность Директор

# dict_ = {"Asan" : "director"}

# def data(dict):
#     for keys, values in dict.items():
#         return(f'Работник {keys} занимает должность {values}')

# print(data(dict_))

 

# Задача 6 (дополнительно)

# Напишите программу, которая будет суммировать все числа, введенные пользователем, игнорируя при этом нечисловой ввод. Выводите на экран текущую сумму чисел после каждого очередного ввода. Ввод пользователем значения, не являющегося числовым, должен приводить к появлению соответствующего предупреждения, после чего пользователю должно быть предложено ввести следующее число. Выход из программы будет осуществляться путем пропуска ввода. Удостоверьтесь, что ваша программа корректно обрабатывает целочисленные значения и числа с плавающей запятой. 

# Пример:
# Введите число: 1
# Сумма: 1
# Введите число: 2
# Сумма: 3
# Введите число: 5
# Сумма: 8
# Введите число: кукарача
# Ошибка, введите только числа
# Введите число: 12
# Сумма: 20 (т.е. сумма не обнуляется, а продолжает "считать" (8 + 12 = 20)

# def suma():
#     sum_ = 0

#     while True:
#         user = input('Введите число: ')
#         try:
#             number = float(user)
#             sum_ += number
#             print(f"Сумма: {sum_}")
#         except ValueError:
#             print("Ошибка, вводите только числа.")
        
#         if user == "":
#             break

# suma()            

