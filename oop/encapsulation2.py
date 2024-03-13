# Аннотация свойств (@property(getter, setter))

# class Person:
#     __name = 'John'
#     __age = 22

#     @property
#     def name(self):
#         """The name property(getter)"""
#         print(self.__name)

#     @name.setter
#     def name(self, value):
#         """The name property(setter)"""
#         if not isinstance(value, str):
#             print('Invalid value for name') 
#         else:
#             print(f'Setter, {value}')
#             self.__name = value

#     @property
#     def age(self):
#         print(self.__age)

#     @age.setter
#     def age(self, value):
#         if not isinstance(value, int) or value not in range(0,130):
#             print('Invalid Value for age')
#         else:
#             self.__age = value

# obj = Person()
# obj.name
# obj.name = 'Din Winchester'
# obj.name
# obj.age
# obj.age = 131
# obj.age = 150
# obj.age = 30
# obj.age

# -----------------------------------------------------------------------------------------------------------------------
# read, write, delete

# class Circle:
#     def __init__(self, radius) -> None:
#         self._radius = radius

#     def _get_radius(self):
#         print('getter, _get_radius')

#     def _set_radius(self, value):
#         print('setter, _set_radius')
#         if not isinstance(value, (int, float)):
#             print('radius must be an int or float object')
#         else:
#             self._radius = value

#     def _del_radius(self):
#         print('deleter, _del_radius')
#         answer = input('Are you sure(yes/no)?')
#         if answer.lower().strip() == 'yes':
#             print('deleted')
#         else:
#             print('not deleted')

#     radius = property(fget=_get_radius, fset=_set_radius, fdel =_del_radius, doc = 'radius property')

# obj = Circle(5)
# print(obj.radius)
# obj.radius = 24
# print(obj.radius)

# -----------------------------------------------------------------------------------------------------------------------

# class CoorditaeWriteError(Exception):
#     pass

# class CordinateProperty:
#     def init(self,x,y):
#         self._x = x
#         self._y = y

#     @property
#     def _get_coordinates(self):
#         return (self._x,self._y)

#     def _set_coordinates(self,value):
#         if not isinstance(value,tuple) or len(value) !=2 :
#             raise CoorditaeWriteError("Coordinates must be a tuple of two numbers")
#         elif not all(isinstance(i,(int, float)) for i in value):
#             raise CoorditaeWriteError("All elements of the coordinates must be numbers")
    
#     @_get_coordinates.setter
#     def get_coordinates(self,value):
#         raise CoorditaeWriteError('y coordinate is read-only')
#     @_get_coordinates.deleter
#     def remove_coordinates(self):
#         print('Not implemented yet')

# obj = CordinateProperty(42.12123,-12.12313)
# print(obj.get_coordinates)

# import hashlib
# import os

# class User:
#     def __init__(self, username, password) -> None:
#         self.username = username
#         self.__password = password

#     @property
#     def password(self):
#         raise AttributeError('Password is write-only')
    
#     @password.setter
#     def password(self, value):
#         if not isinstance(value, str) or len(value) < 0:
#             raise ValueError('Invalid value for password!')
#         salt = os.urandom(32)
#         self.__password = hashlib.pbkdf2_hmac('sha256', value.encode('utf-8'), salt,  100_000)

# john = User('JohnSnow', 'secretkey')
# # print(john.password)
# john.password = 'JohnSnowTheBest'
# print(john._User__password)







