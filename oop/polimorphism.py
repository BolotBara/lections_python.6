# функция полиморфизм -> len():_len_

# print(len('Makers'))
# print(len([1,2,3,4,5,6]))
# print(len({1:2,1:2,1:2,1:2}))

# +(_add__) - метод
# print(5+5)
# print('5'+'5')
# print([5]+[5])

# Полиморфизм - способность функции(метода) использоваться для разных типов(классов)
# Широко распространенное определение: 'оидн интерфейс - много реализации'
# list.oop
# set.oop
# dict.oop

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f'It\'s a cat. Cats name is {self.name}, age: {self.age}')

#     def make_sound(self):
#         print('meow, meow!')

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f'It\'s a dog. Dogs name is {self.name}, age: {self.age}')

#     def make_sound(self):
#         print('bak,bak!')

# cat = Cat('Garfild', 5)
# dog = Dog('Pluto', 5)

# for obj in (cat, dog):
#     obj.info()
#     obj.make_sound()

from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name) -> None:
        self.name = name

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def fact(self):
        pass

class Square(Shape):
    def __init__(self, length)->None:
        super().__init__('Квадрат')
        self.length = length

    def area(self):
        return super().area()
    
    def fact(self):
        return 'У квадрата все стороны равны и углы равны 90 градусам!'


class Circle(Shape):
    def __init__(self, radius)->None:
        super().__init__('Окружность')
        self.radius = radius

    def area(self):
        from math import pi
        return pi * self.radius ** 2    
    
    def fact(self):
        return 'Окружность — замкнутая плоская кривая, все точки которой равноудалены от заданной точки, лежащей в той же плоскости, что и кривая: эта точка называется центром окружности. Отрезок, соединяющий центр с какой-либо точкой окружности, называется радиусом; радиусом называется также и длина этого отрезка. !'

a = Square(5)
b = Circle(5)






