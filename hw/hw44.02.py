"""
1)Создайте класс и объявите в нём 3 метода: публичный, защищённый и приватный. Затем создайте экземпляр данного класса и вызовите по очереди каждый из методов.
"""
# писать код здесь
# class Car:
#     def __init__(self) -> None:
#         pass

#     def public(self):
#         print('публичный')
    
#     def _protected(self):
#         print('защищённый')

#     def __private(self):
#         print('приватный')


# car1 = Car()
# car1.public()
# car1._protected()
# car1._Car__private()

"""
2)Определите класс A, в нём объявите метод method1, который печатает строку "Hello World". Затем создайте класс B, который будет наследоваться от класса A. Создайте экземпляр от класса B, и через него вызовите метод method1.
"""
# писать код здесь

# class A:
#     def method1(self):
#         print('Hello World')

# class B(A):
#     def method2(self):
#         super().method1()
        
# cs = B()
# cs.method2()

"""
3)Объявите класс Car, в котором будет приватный атрибут экземпляра speed. Затем определите метод set_speed, который будет устанавливать значение скорости и метод show_speed, с помощью которого Вы будете получать значение скорости.
"""
# писать код здесь

# class Car:
#     def __init__(self):
#         self.__speed = 0

#     def set_speed(self, speed):
#         self.__speed = speed

#     def show_speed(self):
#         return self.__speed

# my_car = Car()
# my_car.set_speed(180)
# print('Скорость:', my_car.show_speed())


"""
4)Перепишите класс Car из предыдущего задания.
Перепишите метод set_speed() с использование декоратора @speed.setter, а метод show_speed() с использованием декоратора @property, для того чтобы можно было работать с данным классом следующим образом:
"""
# писать код здесь

# class Car:
#     def __init__(self):
#         self.__speed = 0

#     @property
#     def speed(self):
#         return self.__speed

#     @speed.setter
#     def speed(self, value):
#         self.__speed = value

# car = Car()
# car.speed = 120
# print(car.speed)


"""
5. Создайте класс Car. Пропишите в init параметры make, model, year, odometer, fuel.
Пусть у показателя odometer будет первоначальное значение 0, а у fuel 70.
Добавьте метод drive, который будет принимать расстояние в км. В самом начале проверьте,
хватит ли вам бензина из расчета того, что машина расходует 10 л / 100 км (1л - 10 км) . Если
его хватит на введенное расстояние, то пусть этот метод добавляет эти километры к значению
одометра, но не напрямую, а с помощью приватного метода __add_distance. Помимо этого
пусть метод drive также отнимет потраченное количество бензина с помощью приватного
метода __subtract_fuel, затем пусть распечатает на экран “Let’s drive!”. Если же бензина не Let’s drive!”. Если же бензина не
хватит, то распечатайте “Let’s drive!”. Если же бензина не Need more fuel, please, fill more!”
"""
# писать код здесь

# class Car:
#     def init(self, make, model, year, odometer = 0, fuel = 70):
#         self.make = make
#         self.model = model
#         self.year = year
#         self._odometer = odometer
#         self._fuel = fuel
    
#     @property
#     def odometer(self):
#         return self._odometer
    
#     def __add_distance(self, new_vall):
#         self._odometer += new_vall

#     def __subtruct_fuel(self, new_vall):
#         self._fuel = self._fuel - new_vall


#     def drive(self, km):
#         if km * 10  > self._fuel:
#             raise  ValueError("Not enough fuel! Please, fill up the tank.")
#         else:
#             print("Let's drive!")
#             self.__add_distance(km)
#             self.__subtruct_fuel(km * 10)
