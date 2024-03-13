"""

1) Создайте класс Class1 с 2 любыми методами. Создайте второй класс Class2, который наследуется от Class1, и определите в новом классе ещё 2 метода. Создайте экземпляр класса Class2. И вызовите у него все 4 метода.

"""

# писать код здесь
# class Class1:
#     def method1(self):
#         print('Hi1')
#     def method2(self):
#         print('Hi2')

# class Class2(Class1):
#     def method3(self):
#         print('Hi3')
#     def method4(self):
#         print('Hi4')

# obj1 = Class2()
# obj1.method1()  
# obj1.method2() 
# obj1.method3()  
# obj1.method4()  

"""

2) Создайте класс A и определите в нём метод method1, который будет печатать строку "Основной функционал". Затем создайте второй класс B, который наследуется от класса A, и дополните method1 таким образом, чтобы он печатал также строку "Дополнительный функционал". Объявите экземпляр класса B и вызовите метод method1.

"""

# писать код здесь
# class A:
#     def method1(self):
#         print('Основной функционал')

# class B(A):
#     def method1(self):
#         super().method1()
#         print('Дополнительный функционал')

# obj = B()
# obj.method1()

"""

3) Создайте класс MyString, который будет наследоваться от str. Определите 2 своих метода:

append, который будет принимать строку и добавлять её в конец исходной

pop, который удаляет из строки последний элемент и возвращает его.

Пример:

# example = MyString('String')

# example.append('hello')

# print(example) -> 'Stringhello'

# print(example.pop()) -> 'o'

# print(example) -> 'Stringhell'

"""

# писать код здесь
# class MyString(str):
#     def append(self, other):
#         return MyString(self + other)

#     def pop(self):
#         popped = self[-1]
#         return popped, MyString(self[:-1])


# example = MyString('String')
# example = example.append('hello')
# print(example) 
# popped, example = example.pop()
# print(popped)  
# print(example) 


"""

4) Создайте класс MyDict который будет наследоваться от встроенного класса dict. Переопределите метод .get() таким образом, чтобы при попытке получении несуществующего ключа по умолчанию он вовзращал строку 'Are you kidding?' вместо None.

"""

# писать код здесь
# class MyDict(dict):
    # def get(self, key, default=None):
        # if key not in self:
            # return 'Are you kidding?'
        # return super().get(key, default)


"""

5) Создайте класс Person который будет описывать человека, а точнее его имя и возраст. Создайте метод display(), который будет выводит данные об этом человеке.

Создайте второй класс Student, который будет наследоваться от класса Person, он должен принимать все атрибуты, которые были определены в родительском классе и добавьте еще один атрибут, который будет описывать направление студента. Создайте метод display_student(), который будет выводить данные об этом студенте.

Объявите экземпляр класса Student, и выведите данные о нём, как о человеке, затем как о студенте.

"""

# class Person:
#     def init(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print(f"Name: {self.name}, Age: {self.age}")

# class Student(Person):
#     def init(self, name, age, direction):
#         super().init(name, age)
#         self.direction = direction
#     def display_student(self):
#         print(f"Name: {self.name}, Age: {self.age}, Direction: {self.direction}")

# student = Student("Alice", 20, "Computer Science")

# student.display()

# student.display_student() 


"""

6) Создайте класс ContactList, который должен наследоваться от встроенного класса list. В нем должен быть реализован метод search_by_name, который должен принимать имя и возвращать список всех совпадений. Создайте экземпляр класса all_contacts и передайте список ваших контактов.

"""

# class ContactList(list):
#     def search_by_name(self, name):
#         return [contact for contact in self if name.lower() in contact.name.lower()]

# class Contact:
#     def init(self, name, phone):
#         self.name = name
#         self.phone = phone

# all_contacts = ContactList([
#     Contact("Alice", "123456789"),
#     Contact("Bob", "987654321"),
#     Contact("Charlie", "456789123"),
#     Contact("David", "789123456")
# ])

# search_results = all_contacts.search_by_name("Alice")
# for contact in search_results:
#     print(f"Name: {contact.name}, Phone: {contact.phone}")

 

"""

7. Создайте класс Smartphone, экземпляры класса должны иметь такие свойства - name, color, memory, battery. battery по умолчанию

должно быть 0. Переопредилите метод str так чтобы при распечатке он выдавал строку с названием и памятью смартфона.

У данного класса также должен быть метод charge, который увеличивает значение батареи на указанную величину.

 

Создайте два дочерних класса от Smartphone - Iphone и Samsung.

У Iphone должен быть дополнительный аттрибут - ios и метод send_imessage - возвращает строку с сообщением и от какого телефона оно было выслано.

А у Samsung должен быть дополнительный аттрибут android и метод show_time, который показывает текущее время.

Создайте объекты от данных классов и примените все методы.

"""
# import datetime

# class Smartphone:
#     def init(self, name, color, memory, battery=0): 
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.battery = battery

#     def str(self):
#         return f"{self.name} - Memory: {self.memory}"

#     def charge(self, amount):
#         self.battery += amount

# class Iphone(Smartphone):
#     def init(self, name, color, memory, ios, battery=0):
#         super().init(name, color, memory, battery)
#         self.ios = ios

#     def send_imessage(self, message):
#         return f"iMessage: {message} from {self.name}"

# class Samsung(Smartphone):
#     def init(self, name, color, memory, android, battery=0):
#         super().init(name, color, memory, battery)
#         self.android = android

#     def show_time(self):
#         now = datetime.datetime.now()
#         return f"Current time: {now.strftime('%H:%M:%S')}"

# iphone = Iphone("iPhone 15 Pro Max", "White", "256GB", "iOS 15")
# samsung = Samsung("Galaxy S24 Ultra 5G", "Black", "128GB", "Android 11")

# print(iphone)
# print(samsung)

# iphone.charge(50)
# samsung.charge(30)

# print(iphone.send_imessage("Hello, how are you?"))

# print(samsung.show_time())

 

"""

8. Создайте класс Spell для магических заклинаний, экземпляры класса имеют два аттрибута - name - название и formula - полное произношение заклинания.

 

У класса есть два метода: get_description() - дает полное описание заклинания и execute() - совершает заклинание.



Переопределите у класса метод str, чтобы он выдавал вам название, формулу и описание вместе, к примеру:

 

Открытие замков: Alohomora

позволяет магу попасть в любую комнату,

способно открыть любую закрытую замочную скважину.

 

Наследуя от класса Spell создайте три заклинания,переопределяя в них родительские методы. Создайте объекты этих трех заклинаний. Вызовите все методы

"""

# class Spell:
#     def init(self, name, formula, description):
#         self.name = name
#         self.formula = formula
#         self.description = description

#     def get_description(self):
#         return self.description

#     def execute(self):
#         print(f"Executing spell: {self.name} - {self.formula}")

#     def str(self):
#         return f"{self.name}: {self.formula}\n{self.description}\n"

# class Alohomora(Spell):
#     def init(self):
#         super().init("Открытие замков", "Alohomora", "Позволяет магу попасть в любую комнату, способно открыть любую закрытую замочную скважину.")

# class Lumos(Spell):
#     def init(self):
#         super().init("Освещение", "Lumos", "Призывает магический свет, освещающий темные места и помогающий в ориентации в ночное время.")

# class Expelliarmus(Spell):
#     def init(self):
#         super().init("Разоружение", "Expelliarmus", "Отбирает у противника его волшебный или немагический артефакт.")

# spell1 = Alohomora()
# spell2 = Lumos()
# spell3 = Expelliarmus()

# print(spell1)
# print(spell1.get_description())
# spell1.execute()

# print(spell2)
# print(spell2.get_description())
# spell2.execute()

# print(spell3)
# print(spell3.get_description())
# spell3.execute()


"""

9. Напишите класс CustomError который наследуется от встроенного класса исключений Exception. Переопределите init таким образом

чтобы через экземпляр класса можно было передавать сообщение и создавать новые виды исключений.

Создайте исключение от этого класса с сообщением:

"ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ"

 

Напишите функцию проверяющую строки на регистр и если строка не написана в верхнем регистре выбросите исключение созданное классом CustomError:

 

Traceback (most recent call last):

  File "inheritance.py", line 121, in <module>

    check_letters(a)

  File "inheritance.py", line 117, in check_letters

    raise capitals_error

main.CustomError: ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ

 

"""

# class CustomError(Exception):
#     def init(self, message):
#         self.m = super().init(message)

# def check_letters(self, string):
#     if not string.isupper():
#         raise CustomError(self.m)

# try:
#     a = "Hello"
#     check_letters(a)
# except CustomError as capitals_error:
#     print(capitals_error)
 

"""

10. Создайте класс Character с помощью которого можно создавать героев для игры. Экземпляры класса должны иметь аттрибут name. У класса должна быть переменная power_list, в которой хранится словарь:

power_list = { 'мудрость': 0, 'харизма': 0, 'интеллект': 0, 'сила': 0, 'ловкость': 0 }

 

Класс должен иметь методы:

give_weapon - выбирает случайное оружие из списка

 

give_role - выбирает случайную роль из списка, к примеру:

["Варвар","Бард", "Клерик", "Боец", "Лесничий", "Паладин", "Чернокнижник"]

 

give_powers, передавая силу и значение можно менять power_list для определенного героя, к примеру:

char1.give_powers('ловкость', 5)

увеличит ловкость вашего героя.

 

Создайте три разных дочерьних класса от класса Character - Elf, Orc, DragonBorn,

дайте каждому из классов уникальный метод и добавьте уникальные аттрибуты экземпляра класса,наследуя init от Character. Создайте несколько героев от этих классов и вызовите их методы и методы родительского класса Character.

"""

# import random

# class Character:
#     power_list = { 'мудрость': 0, 'харизма': 0, 'интеллект': 0, 'сила': 0, 'ловкость': 0 }
#     weapons = ["Меч", "Лук", "Кинжал", "Посох", "Молот"]

#     def init(self, name):
#         self.name = name

#     def give_weapon(self):
#         return random.choice(Character.weapons)

#     def give_role(self):
#         roles = ["Варвар","Бард", "Клерик", "Боец", "Лесничий", "Паладин", "Чернокнижник"]
#         return random.choice(roles)

#     def give_powers(self, power, value):
#         if power in Character.power_list:
#             Character.power_list[power] = value

# class Elf(Character):
#     def init(self, name):
#         super().init(name)
#         self.magic_ability = True

#     def cast_spell(self):
#         return f"{self.name} использует магическое заклинание!"

# class Orc(Character):
#     def init(self, name):
#         super().init(name)
#         self.strength = 10

#     def roar(self):
#         return f"{self.name} рычит и демонстрирует свою силу!"

# class DragonBorn(Character):
#     def init(self, name):
#         super().init(name)
#         self.fire_breath = True

#     def breathe_fire(self):
#         return f"{self.name} выпускает огненный дыхание!"

# elf = Elf("Леголас")
# orc = Orc("Гром")
# dragonborn = DragonBorn("Драконорожденный")

# print(f"{elf.name} получает {elf.give_weapon()} в качестве оружия.")
# print(f"{orc.name} играет роль {orc.give_role()}.")
# elf.give_powers('ловкость', 5)
# orc.give_powers('сила', 15)
# print(f"Параметры героев: {Character.power_list}")

# print(elf.cast_spell())
# print(orc.roar())
# print(dragonborn.breathe_fire())