# 1
# Автомобиль: создайте класс с именем Car. Метод __init__ () класса Car должен содержать три атрибута: brand, year и color. Создайте метод get_auto(), который выводит информацию об автомобиле, и метод get_year, который выводит возраст авто .
# Добавьте атрибут horsepower, который равен 85.
# Напишите метод add_horsepower, который всем машинам будет добавлять по 20 л/с, а машинам Mers, Bmw, Poshe по 40 л/с
# Создайте на основе своего класса экземпляр с именем bmw . Выведите три атрибута по отдельности, затем вызовите все методы.
# Два авто: начните с класса из вышеописанного упражнения. Создайте 2 разных экземпляра, вызовите для каждого экземпляра метод get_auto
# class Car:
#     def __init__(self, brand, year, color):
#         self.brand = brand
#         self.year = year
#         self.color = color
#         self.horsepower = 85
    
#     def get_auto(self):
#         print('Brand:', self.brand)
#         print('Year:', self.year)
#         print('Color:', self.color)
    
#     def get_year(self, current_year):
#         age = current_year - self.year
#         if age == 1:
#             print(f'Автомобилю уже {age} год.')
#         else:
#             print(f'Автомобилю уже {age} лет.')
    
#     def add_horsepower(self):
#         if self.brand in ['Mers', 'Bmw', 'Poshe']:
#             self.horsepower += 40
#         else:
#             self.horsepower += 20


# bmw = Car('BMW', 2019, 'Black')

# print('Brand:', bmw.brand)
# print('Year:', bmw.year)
# print('Color:', bmw.color)
# print('Horsepower:', bmw.horsepower)

# bmw.get_auto()
# bmw.get_year(2024)
# bmw.add_horsepower()
# print('Новая скорость:', bmw.horsepower)


# 2
# Студенты: создайте класс с именем Student. Создайте атрибуты name, age, course. Напишите метод get_student(), который выводит сводку с информацией о студенте . Создайте еще один метод get_birth_year() для вывода информации о годе рождения студента.
# Создайте несколько экземпляров, представляющих разных студентов. Вызовите оба метода для каждого студента.

# class Student:
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course
    
#     def get_student(self):
#         print('Имя:', self.name)
#         print('Возраст:', self.age)
#         print('Курс:', self.course)
    
#     def get_birth_year(self, current_year):
#         birth_year = current_year - self.age
#         print(f"{self.name} родился в {birth_year}")

# student1 = Student('Иван', 20, 3)
# student2 = Student('Саня', 22, 4)

# student1.get_student()
# student1.get_birth_year(2024)
# print()
# student2.get_student()
# student2.get_birth_year(2024)

















