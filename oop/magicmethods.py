# magic methods - магические методы
# dunder methods (double underscore) -> init
# служебные методы

# Магия(фишка) заключается в том, что эти методы запускаются без прямого обращения к ним, определенные методы могут отвечать за определенные операторы.

# Магические методы сравнения
# eq(self, other) -> 5 == 8
                        #  5eq(8)
# ne -> !=
# lt -> <
# gt -> >
# le -> <=
# ge -> >=

# print('15' > 'ABC')

# class Word(str):
#     def __new__(cls, obj):
#         obj = obj.replace(' ', '')
#         return super().__new__(cls, obj)

#     def __init__(self, obj) -> None:
#         super().__init__()
#         self.obj = obj

#     def __gt__(self, other):
#         print('gt worked')
#         print(self, '---', other)
#         if len(self) > len(other):
#             return self
#         elif len(self) < len(other):
#             return other
#         else:
#             return 'eq'
        
#     def __it__(self, other) -> bool:
#         return len(self) < len(other)
    
#     def __eq__(self, other) -> bool:
#         return len(self) == len(other)

# obj = Word('           Hello John    ')
# obj2 = Word(' God i  fy')

# print(obj > obj2)
# print(obj < obj2)
# print(obj == obj2)

# ------------------------------------------------------------------------------------------------

# + - / * // % **

# + -> __ad__
# - -> __sub__
# * -> __mul__
# // -> __floordiv__
# / -> __div__(py2) -> __truediv__(py3)
# % -> __mod__
# ** -> __pow__

# class Cifra:
#     def __new__(cls, *args, **kwargs):
#         print(cls, '!!!!')
#         number = abs(args[0])
#         instance = super().__new__(cls)
#         instance.nuber = number
#         return instance
    
#     def __add__(self, other):
#         print('add worked')
#         res = self.number + other.number
#         print(f'Result: {self.number} + {other.number} = {res}')     
#         return res

# value1 = Cifra(-117)
# value2 = Cifra(53)
# res = value1 + value2
# print(res)

# ------------------------------------------------------------------------------------------------

# from random import choice

# class Dog:
#     def sound(self):
#         print('Bark')

# class Cat:
#     def sound(self):
#         print('Meow meow!')

# class Horse:
#     def sound(self):
#         print('Igo-go-go')

# class Pet:
#     def __new__(cls):
#         pet = choice([Dog, Cat, Horse])
#         self = super().__new__(pet)
#         print(f'I\'m {type(self).__name__}')
#         return self

#     def __init__(self) -> None:
#         print('Pet never was called!')

# pet = Pet()
# pet.sound()

# ------------------------------------------------------------------------------------------------

# SIMGLETON

# class Singleton:
#     _instance = None

#     def __new__(cls):
#         if not cls._instance:
#             cls.instance = super().__new__(cls)
#         return cls.instance

#     def __str__(self) -> str:
#         return str(id(self))

# a = Singleton()
# b = Singleton()
# print(a, b)
# print(a is b)
# obj = Singleton()
# obj1 = Singleton()
# print(obj, obj1)

# ------------------------------------------------------------------------------------------------

# from itertools import repeat
# from random import choice, randint

# class Kopilka:
#     def __init__(self) -> None:
#         self.total = 0
#         self.coins = []

#     def add_coin(self, coin):
#         self.total += coin
#         self.coins.append(coin)

#     def __len__(self):
#         return len(self.coins)

#     def __getitem__(self,index):
#         return self.coins[index - 1]

# obj = Kopilka()
# print(obj.coins)
# print(obj.total)

# print(len(obj))
# for f in repeat(choice, randint(89, 155)):
#     obj.add_coin(f([1,3,5,10]))
# obj.add_coin(3)
# obj.add_coin(5)
# obj.add_coin(10)
# print(len(obj))
# print(obj[1])
# print(obj[2])
# print(obj[3])




