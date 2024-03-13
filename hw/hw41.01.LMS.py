# 1. Создайте класс BankAccount, в конструкторе которого определена переменная
# экземпляра класса balance = 0. Определите метод withdraw с параметром amount,
# который будет отнимать сумму от баланса и возвращать текущий баланс. Также
# добавьте метод deposit, который также имеет параметр amount и соответсвенно
# добавляет сумму к балансу, возвращает баланс.

# class BankAccount:
#     def __init__(self):
#         self.balance = 0

#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             return self.balance
#         else:
#             print('Недостаточно средств')

#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance

# a = BankAccount()
# print(a.balance)


# 2. Вам дан такой код:

# winner1 = Nobel("Литература", 1971, "Пабло Неруда")
# print(winner1.category, winner1.year, winner1.winner)
# print(winner1.get_year())

# winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ")
# print(winner2.category, winner2.year, winner2.winner)
# print(winner2.get_year())

# который выводит в терминал такие значения:

# Литература 1971 Пабло Неруда
# выиграл 50 лет назад

# Литература 1994 Кэндзабуро Оэ
# выиграл 27 лет назад

# Напишите класс Nobel и метод класса get_year() таким образом, чтобы данный вам код вывел указанные значения в терминале. Даты внутри класса не хардкодить.

# from datetime import datetime

# class Nobel:
#     def __init__(self, name, year, aftor):
#         self.name = name
#         self.year = year
#         self.aftor = aftor

#     def get_year(self):
#         years_ago = datetime.now().year - self.year
#         return f'выиграл {years_ago} лет назад'

# winner1 = Nobel('Литература', 1971, 'Пабло Неруда')
# winner2 = Nobel('Литература', 1994, 'Кэндзабуро Оэ')

# print(winner1.name, winner1.year, winner1.aftor)
# print(winner1.get_year())

# print(winner2.name, winner2.year, winner2.aftor)
# print(winner2.get_year())


# 3. Создайте класс Password, экземеплярами класса являются пароли в виде строк. У класса должен быть метод validate для валидации пароля:
# - пароль должен быть минимум 8 символов, но меньше 15
# - пароль должен содержать цифры
# - пароль должен содержать буквы
# - пароль должен содержать хотя бы один из символов:
#     '@', '#', '&', '$', '%', '!', '~', '*'

# если одно из условий не выполнено, выводите кастомное исключение, 
# если же все условия выполнены метод validate должен возвращать строку: 'Ваш пароль сохранен'.

# Также переопределите метод str, чтобы при попытке распечатать
# сам пароль, вам выдавалась строка из звездочек,
# к примеру пароль - 'joe@123456'
# в терминале выйдет - ******

# class Password:
#     def __init__(self) -> None:
#         pass
#     def validate(self, password:str)->bool:
#         if len(password) < 8 or len(password) > 15:
#             raise ValueError('Пароль должен быть минимум 8 символов, но больше 15!')
#         if not any(char.isdigit() for char in password):
#             raise ValueError('Пароль должен содержать цифры!')
#         if not any(char.isalpha() for char in password):
#             raise ValueError('Пароль должен содержать буквы!')
#         special_chars = ['@', '#', '&', '$', '%', '!', '~', '*']
#         if not any(char in special_chars for char in password):
#             raise ValueError('Пароль должен содержать хотябы один спецсимвол(@, #, &, $, %, !, ~, *)')
#         return True

#     def __str__(self) -> str:
#         return '*' * len(self.__pass)


# pwd = Password()
# try:
#     pwd.validate('joe@123456')
# except ValueError as e:
#     print(e)
# else:
#     print('Ваш пароль сохранен')


# 4. Создайте класс Math, экземпляром которого должно быть число.
# У классa Math должно быть 3 метода:
# - get_factorial - выводит факториал числа
# - get_sum - выводит сумму цифр числа
# - get_mul_table - выводит таблицу умножения для числа до 10. Создайте экземпляр класса и примените к нему все методы. 

# import math

# class Math:
#     def __init__(self) -> None:
#         pass

#     def get_factorial(self, num:int)->int:
#         self.num = num
#         return math.factorial(self.num)

#     def get_sum(self, num:int)->int:
#         self.num = num
#         return sum(map(int, str(self.num)))


#     def get_mul_table(self, num:int)->int:
#         self.num = num
#         table = []
#         for i in range(1, 11):
#             cell = f"{self.num} x {i} = {self.num * i}"
#             table.append(cell)
#         return '\n'.join(table)


# m = Math()
# print(f'Факториал: {m.get_factorial(5)}')
# print(f'Сумма цифр: {m.get_sum(1234567890)}')
# print(f'\nМножество умножений:\n{m.get_mul_table(9)}')


# 5. Создайте класс ToDo, экземплярами данного класса являются строки-задачи(сходить в кино, сделать домашку, выгулять собаку и.т.д)

# У класса есть метод give_priority который записывает вашу задачу в список(переменная класса) с ключом в виде числа, 
# приоритет который вы даете вашей задаче -
# к примеру {3: 'сходить в кино'}
# приоритет сходить в кино у вас не самый высокий.

# У класса должен быть метод list_of_tasks, который выдает вам список отсортированных задач 
# по приоритету:
# [(1, 'сделать домашку'), (2, 'выгулять собаку'), (3, 'сходить в кино')]


# class Todo:
#     tasks = {}
#     def give_priority(self, task, priority):
#         Todo.tasks[priority] = task

#     def list_of_tasks(self):
#         sorted_tasks = sorted(Todo.tasks.items())
#         return sorted_tasks

# obj = Todo()

# obj.give_priority('сходить в кино',3)
# obj.give_priority('поехать на бали',4)
# obj.give_priority('понюхать кокс',5)

# sorted_task = obj.list_of_tasks()
# print('List of tasks: ',sorted_task)














