# области видимости и пространства имен(scopes)
# технология, котораяа определет контекст имени в рамках которого мы иожем ее использовать.

# a = 5
# def func():
#     b = 10
#     print(a)
#     print(b)

# func()
# print(b)

# built-ins(встроееная область видимости)-print(), len()
# global(глобальная)-область одного файла
# <enclosed>(замкнутая(не локальная, non local))
# local(локальная) -> область внутри одной функции 

# a = 10 # global
# print # buil-in
# def hello(): # global
#     a = 'Hello' # local
#     print(a, 'local, inside in func!')

# hello()
# print(a, 'global')
# len()

# LEGB - local enclosed global built-in

# -----------------------------------------------------------------------

# enclosed
# замкнутое простанство имен - локальное пространство есть вложенная (внутреннее) пространство

# x = 'global'
# print(x, '1') # global

# def enclosed(): # global
#     x = 'enclosed'

#     def local(): # enclosed
#         x = 'local'
#         print(x, '3') # local

#     print(x, '2') # enclosed
#     local()
#     print(x, '4') # enclosed

# enclosed() 
# print(x, '5') # global

# var = 0

# def increment():
#     global var
#     var = var + 1
#     if var < 5:
#         increment()

# increment()
# print(var)

# global -> позволяет изменять значение глобальной переменной внутри локальной области
# nonlocal -> позволяет изменять значение не локальной (замкнутой) переменной внутри локальной области

# def  counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment

# c_steps = counter()
# c_jumps = counter()
# print(c_steps)
# for _ in range(1, 10000):
#     c_steps()

# print(c_steps(), 'steps')
# print(c_jumps(), 'jump')
# print(c_jumps(), 'jump')
# print(c_jumps(), 'jump')


























