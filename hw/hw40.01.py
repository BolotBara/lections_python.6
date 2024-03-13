"""
1) Создайте класс Circle, с переменными класса задающие по умолчанию цвет круга - синий, и число Пи(3.14). Экземпляры класса Circle в свою очередь должны иметь обязательный аттрибут - радиус. Также класс должен иметь метод расчета площади круга. Создайте экземпляр класса, переопределите цвет экземпляра и расчитайте площадь фигуры.
"""
# писать код здесь
# import math

# class Circle:
#     color = 'синий'
#     pi = 3.14
    
#     def __init__(self, radius):
#         self.radius = radius

#     def calculate(self):
#         return self.pi * self.radius ** 2

# radius = float(input('Введите радиус круга: '))
# circle = Circle(radius)
# print(f'Площадь круга с радиусом {radius} - {circle.calculate()}, {circle.color}.')
# circle.color = 'крансый'
# print(f'Площадь круга с радиусом {radius} - {circle.calculate()}, {circle.color}.')


"""
2) Создайте класс для песен Song. Каждая песня имеет название, автора и год выпуска. Добавьте три метода show_author, show_title, show_year, выводящие утверждения о каждом атрибуте экземпляра класса Song, например: "Эта песня вышла в 2010 году". Создайте экземпляр класса с вашей любимой песней и примените все методы.
"""
# писать код здесь

# class Song:
#     def  __init__(self, title, artist, year):
#         self.title = title
#         self.artist = artist
#         self.year = year

# song1 = Song('Song1', 'Artist1', 2010)
# print(f'{song1.title} - {song1.artist}: Эта песня вышла в {song1.year} году')


"""
3) Создайте класс Taxi, объекты которого имеют такие атрибуты как название компании, стоимость посадки, стоимость за каждый пройденный километр. Также добавьте к классу метод расчитывающий стоимость поездки. Создайте три экземпляра класса Taxi для трех разных компаний Namba, Yandex и Jorgo и расчитайте стоимость поездки на каждом из них.
"""
# писать код здесь

# class Taxi:
#     def  __init__(self, сompany_name,landing_cost,kilometer_cost ):
#         self.сompany_name = сompany_name
#         self.landing_cost = landing_cost
#         self.kilometer_cost = kilometer_cost

#     def price(self, km):
#         return self.landing_cost + km * self.kilometer_cost
        
# taxi1 = Taxi('Namba',15, 10 )
# taxi2 = Taxi('Yandex',20, 15 )
# taxi3 = Taxi('Jorgo',25, 20 )

# km = float(input('Введите количество пройденных километров: '))
# print(f'Стоимость поездки в компании {taxi1.сompany_name}: {taxi1.price(km)}')
# print(f'Стоимость поездки в компании {taxi2.сompany_name}: {taxi2.price(km)}')
# print(f'Стоимость поездки в компании {taxi3.сompany_name}: {taxi3.price(km)}')


"""
4) Создайте класс телефонной книги. У контактов должны быть имена и фамилии и номер телефона. Также создайте метод get_info, который выводит информацию о контакте в следующем виде: "Контакт: Иван Петров, телефон: +996555777888".
Затем объявите экземляр класса и вызовите метод.
"""
# писать код здесь

# class Telebook:
#     def __init__(self, first_name, last_name, nomber):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.nomber = nomber

#     def get_info(self):
#         return f'Контакт: {self.first_name} {self.last_name}, телефон: {self.nomber}'

# phonebook = Telebook('Иван', 'Иванов', '+79261234567')
# print(phonebook.get_info())


"""
5) Напишите класс Salary для расчета налогов на заработную плату. У класса должна быть обязательная переменная класса - процент налога от зарплаты - 8%. Объекты класса должны иметь сумму зарплаты и стаж работы в качестве атрибутов. Также у класса должен быть метод расчитывающий сумму налога заплаченного за весь стаж работы. Создайте экземпляр класса и посчитайте сумму вашего налога.
"""
# писать код здесь

# class Salary:
#     procent = 8
#     def __init__(self, salary, experience):
#         self.salary = salary
#         self.experience = experience

#     def calculate(self):
#         total_ = self.salary * self.procent / 100 * self.experience
#         return total_

# ivan_salary = Salary(1000, 5)
# print(f"Сумма налога, уплаченная за {ivan_salary.experience} лет работы: {ivan_salary.calculate()} рублей")



# Создайте класс Soda принимающий 1 аргумент при инициализации (отвечающий за добавку к выбираемому лимонаду).
# В этом классе реализуйте метод show_my_drink(), выводящий на печать «Газировка и {ДОБАВКА}» в случае наличия добавки, а иначе отобразится следующая фраза: «Обычная газировка».



# Создайте класс Student. При создании его экземпляра, мы должны записать имя и фамилию студента в соответствующие переменные объекта. В классе должны быть:
#  1 переменная объекта books = []
#  2 переменная объекта “knowledge” со значением по умолчанию 0
#  3 метод read_book, который принимает название книги, добавляет книгу в books, добавляет 100 баллов в knowledge
#  4 метод do_homework, который при вызове добавляет 10 баллов в knowledge
#  5 Создайте экземпляры, вызовите методы.

# 6. Создайте класс имеющий атрибут "дата рождения" и автоматически просчитываемый возраст по входящей дате рождения. Используйте модуль time/datetime

# class Soda:
#     soda = 'soda'
#     def __init__(self, topping):
#         self.__topping = topping
#     @property
#     def topping(self):
#         return self.__topping
#     @topping.setter
#     def topping(self, new_topping):
#         self.__topping = new_topping

#     def show_my_drink(self):
#         return f"{Soda.soda} add {self.topping}"
# fanta = Soda('fanta')
# cola = Soda('cola')
# print(fanta.show_my_drink())
# print(cola.show_my_drink())


# class Student:
#     def __init__(self, fio):
#         self.fio = fio
#         self.books = []
#         self.knowledge = 0
#     def read_book(self, book):
#         self.books.append(book)
#         self.knowledge += 100
#     def do_homework(self):
#         self.knowledge += 10

# std = Student( "Ivan Ivanov")
# std.read_book("Physics")
# print(std.books)
# print(std.knowledge)
# std.do_homework()
# print(std.knowledge)
# std.read_book("Math")
# print(std.knowledge)
# print(std.books)



# from datetime import datetime, date

# class Person:
#     def __init__(self, birth_date):
#         self.birth_date = birth_date

#     @property
#     def age(self):
#         today = date.today()
#         age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
#         return age

# birth_date = datetime(1990, 5, 15)
# person = Person(birth_date)

# Получение и вывод возраста
# print(f"Возраст: {person.age} лет")

# Задание 2: Класс "Студент"

# Задача: Определите класс Студент с атрибутами имя и оценки (список оценок). Добавьте методы для добавления оценки к списку оценок и метод для расчета среднего балла.

# Пример использования:

# студент = Студент("Иван")
# студент.добавить_оценку(5)
# студент.добавить_оценку(4)
# print(студент.расчет_среднего()) -> 4.5
# class Студент:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def  добавить_оценку(self, mark):
#         self.marks.append(mark)
    
#     def расчет_среднего(self):
#         ave =  sum(self.marks)/len(self.marks)
#         return ave


# студент = Студент("Иван", [4,4])
# студент.добавить_оценку(5)
# студент.добавить_оценку(4)
# print(студент.расчет_среднего())


# Задание 1: Класс "Комната" и "Дом"
# Цель: Практика в создании взаимодействующих объектов и управлении ими.
# Задача: Создайте класс Комната с атрибутами название, ширина и длина. Добавьте метод, который вычисляет площадь комнаты. Затем создайте класс Дом, который содержит список комнат. В классе Дом должны быть методы для добавления комнаты и вычисления общей площади дома.
# class  Room:
#     def __init__(self, number, width, lenght):
#         self.number = number
#         self.width = width
#         self.lenght = lenght
#         self.calculate_area()
#     def calculate_area(self):
#         return self.lenght * self.width
    

# class House:
#     def __init__(self, rooms):
#         self.rooms = rooms

#     def add_room(self, room):
#         self.rooms.append(room)

#     def house_area(self):
#         total_area = sum([r.calculate_area() for r in self.rooms])
#         return total_area


# house = House([Room(1, 100, 20), Room(2, 80, 30)])
# print(f'Area of the house: {house.house_area()}')
# house.add_room(Room(1, 100, 20))
# print(f'Area of the house: {house.house_area()}')
# Задание 3: Класс "Библиотека" и "Книга"
# Цель: Работа с коллекциями объектов и их методами.

# Задача: Расширьте класс Книга из предыдущего задания, добавив атрибут количество. Создайте класс Библиотека, который будет содержать список книг. В классе Библиотека реализуйте методы для добавления книги (с учетом уже существующих тайтлов), удаления книги по названию, и поиска книг по автору.

# class Books:
#     def __init__(self, autor, name, count):
#         self.autor = autor
#         self.name = name 
#         self.count = count

# class Librari:
#     def __init__(self):
#         self.books = []
#     def add_book(self, book):
#         for existing_book in self.books:
#             if existing_book.name == book.name and existing_book.autor == book.autor:
#                 existing_book.count += book.count
#                 break
#         else:
#             self.books.append(book)
#     def remove_book(self, book_name):
#         for i, book in enumerate(self.books):
#             if book.name == book_name:
#                 if book.count > 1:
#                     book.count -= 1
#                 else:
#                     del self.books[i]
#                 return
#         print("The book is not found.")

#     def serch_book_of_aoutor(self,aoutor):
#         result = [b.name for b in self.books if b.autor == aoutor]
#         return result
#     def show_all_books(self):
#         return [[b.autor,b.name, b.count] for b in self.books]
    

# create_library = Librari()
# create_library.add_book(Books("Rowling","Harry Potter and the Philosopher's Stone",4))
# create_library.add_book(Books("Rowling","Harry Potter and the Philosopher's Stone",2))
# create_library.add_book(Books("Anarbek","Python",4))
# print(create_library.show_all_books())
# create_library.remove_book("Python")
# print(create_library.show_all_books())
# print(create_library.serch_book_of_aoutor("Rowling"))

# Задание 4: Класс "Магазин" и "Продукт"
# Цель: Изучение принципов инкапсуляции и взаимодействия объектов.

# Задача: Создайте класс Продукт с атрибутами название, цена и категория. Затем создайте класс Магазин, который будет содержать список продуктов. В Магазине реализуйте методы для добавления продукта, удаления продукта по названию, и метод, который выводит список продуктов определенной категории.

# class Product:
#     def __init__(self, name, price, category):
#         self.__name = name
#         self.__price = price
#         self.__category = category

#     @property
#     def name(self):
#         return self.__name

#     @property
#     def price(self):
#         return self.__price

#     @property
#     def category(self):
#         return self.__category

#     @category.setter
#     def category(self, value):
#         if not isinstance(value, str) or len(value) == 0:
#             raise ValueError('Category must be a non-empty string')
#         self.__category = value


# class Shop:
#     def __init__(self):
#         self.products = []

#     def add_product(self, product):
#         if isinstance(product, Product):
#             self.products.append(product)
#         else:
#             print("The object is not an instance of the class 'Product'")

#     def show_all_products(self):
#         for i, product in enumerate(self.products, 1):
#             print(f"Product {i}:")
#             print(f"Name: {product.name}")
#             print(f"Price: {product.price}")
#             print(f"Category: {product.category}\n")

#     def search_by_category(self, category):
#         found_products = [product for product in self.products if product.category.lower() == category.lower()]
#         if found_products:
#             print(f"\nFound {len(found_products)} products in the category '{category}':")
#             for product in found_products:
#                 print(f"Name: {product.name}, Price: {product.price}")
#         else:
#             print(f"No products found in the category '{category}'.")



# shop = Shop()
# shop.add_product(Product("IPhone X", 1000, "Electronics"))
# shop.add_product(Product("Samsung Galaxy", 800, "Electronics"))
# shop.add_product(Product("Dress", 50, "Clothing"))

# shop.show_all_products()

# shop.search_by_category("Electronics")


# Задание 5: Класс "Пользователь" и "УчетнаяЗапись"
# Цель: Глубокое понимание взаимодействия классов и управления состоянием.

# Задача: Создайте класс Пользователь с атрибутами имя, фамилия и email. Создайте класс УчетнаяЗапись, который будет содержать пользователя, логин, пароль и баланс. В классе УчетнаяЗапись реализуйте методы для изменения пароля, пополнения баланса и совершения платежа, проверяя достаточность средств на балансе.

# class User:
#     def __init__(self, fio, email):
#         self.fio = fio
#         self.email = email
# class Account:
#     def __init__(self, user, login, password, balance):
#         self.user = user
#         self.login = login
#         self.password = password
#         self.balance = balance
#     def  change_password(self, new_pass):
#         self.password = new_pass
#     def make_deposit(self, amount):
#         self.balance += amount
#     def make_withdrawal(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             return "Not enough money on account."


# some_user = User('Bolot', 'bolot@gmail.com')
# some_user_account = Account(some_user, 'bolot45', 'qwerty987654321', 500)
# print(some_user_account.balance) # 500
# some_user_account.make_deposit(100)
# print(some_user_account.balance) # 600
# some_user_account.change_password('dfsde2434')
# print(some_user_account.password) # dfsde2434
# print(some_user_account.make_withdrawal(200))
# print(some_user_account.balance)


# another_user = User('John Doe', 'john.doe@mail.ru')
# another_user_account = Account(another_user, 'johndoe', 'mypassword123', 1000)
