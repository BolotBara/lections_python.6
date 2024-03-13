# class Student:
#     univer = 'MIT'
#     def __init__(self,name)-> None:
#         self.name = name
#         self.books = []
#         self.languages = {}
#         self.knowledge = 0
#         self.is_ready_work = False

#     def  add_points(self, point):
#         self.knowledge +=point
#         if self.knowledge > 500 and not self.is_ready_work:
#             self.is_ready_work=True
#             print(f'{self.name} gets 500 points and is ready to work!')

#     def read_book(self, book_name):
#         self.add_points(50)
#         self.books.append(book_name)
    
#     def do_progect(self):
#         self.add_points(100)

#     def learn_lang(self, language, percent):
#         if percent not in range(70,101):
#             print('Invalid points for lang')
#         else:
#             self.language[language] = percent
#             self.add_points(percent)

# st1 = Student('John Snow')
# st2 = Student('Din Winchester')

# print(st1.name)
# print(st2.name)

# print(f'Before study {st1.name}: {st1.books}, {st1.languages}, {st1.knowledge}')
# print(f'Readu to work: {st1.is_ready_work}')

# st1.read_book('Grokam algoritmy')
# st1.read_book('Python from beginer to advanced')
# st1.read_book('Algoritms and data structures')
# st1.read_book('Martin Eden')

# st1.do_progect()
# st1.do_progect()

# st1.learn_lang('Python',60)
# st1.learn_lang('Python',90)
# st1.learn_lang('JS',90)

# st1.do_progect()

# print(f'After study {st1.name}: {st1.books}, {st1.languages}, {st1.knowledge}')
# print(f'Readu to work: {st1.is_ready_work}')

# -----------------------------------------------------------------------------------------------------------------------

# class Car:
#     def __init__(self, brand, model) -> None:
#         self.brand = brand
#         self.model = model

#     def show_info(self):
#         return f'{self.brand} -> {self.model}'
    
#     def __str__(self) -> str:
#         return f'{self.brand} -> {self.model}'

# obj = Car('BMW', '8 series')
# print(obj)
# ob1 = Car('Honda', 'Fit')
# print(ob1)
# obj2 = Car('Mercedes-Benz', 'w221')
# print(obj2)

# -----------------------------------------------------------------------------------------------------------------------

# class Soda:
#     def __init__(self, ingredient = None):
#         if isinstance(ingredient, str):
#             self.ingredients = ingredient
#         else:
#             self.ingredients = None

#     def __str__(self) -> str:
#         return 'Normal one!' if not self.ingredients else f'Gazirovka iz {self.ingredients}' 

# a = Soda(1231)
# b = Soda(True)
# print(a,b)

# dushes = Soda('Grusha')
# limonad = Soda('Malina')
# print(dushes, limonad)

# -----------------------------------------------------------------------------------------------------------------------

# import random

# class Sniper:
#     health = 100

#     def __init__(self, name) -> None:
#         self.name = name

#     def __str__(self) -> str:
#         return self.name

#     def shoot(self, other):
#         other.health -=20
#         print(f'Атаковал {self}')
#         print(f'У {other} осталось {other.health}')

# sniper1 = Sniper('Simo Hyohy') 
# sniper2 = Sniper('Roza Shanina') 

# while sniper1.health and  sniper2.health:
#     choice = random.randint(1,2)
#     sniper1.shoot(sniper2) if choice == 1 else  sniper2.shoot(sniper1)
#     print()

# print(f'{sniper1 if sniper1.health else sniper2} won the game!')



