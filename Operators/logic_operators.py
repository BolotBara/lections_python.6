# 17.01.2023 
# Bolot
# 10 - 12: 
# Прошли тему логические операторы(logic operators) 
# Операторы сравнения
# Условные операторы
# Логические операторы
# 12 - 18: 
# Усвоение материала и выполнение домащнего задания прошло успешно

# Операторы сравнения
# Условные операторы
# Логические операторы

# Операторы сравнения:
# <, >, ==(равно), !=(не равно), <=, >=

# 5 < 1 --> False
# 7 < 9 --> True

# print('ABC1234124' > 'abc123')

# a = 'A'
# b = 'B'
# print(ord(a), ord(b)) вытаскивает аский код по буквам буквам
# num = 98
# print(chr(num)) вытаскивает аский код по цифрам

# Условные операторы
# if 
# elif
# False

# if <condition>:
#     <body if> # сработает если в condition if придет True
# [elif] <condition>:
#     <body elif> 
# [else]:
#     <body else> # сработает если во всех выше стоящих условиях пришло False

# string = input('Enter smt: ').lower()

# print(string)
# if string == 'hello':
#     print('Hello, it\'s me, I was wondering if after all these years you\'d like to meet!' )
# elif string == 'john':
#     print('Wellcome back John Snow! The King of North' )
# elif string == 'abra-kadabra':
#     print('Sim salabim kadabra!' ) 
# else:
#     print('No match found!')

# создание входа - raise ValueError() - выводит ошибку и останавливает вход
# print('Registration form')
# email = input('Enter your emails: ')
# if '@' not in email:
#     raise ValueError('Email is Invalid! @ - not be!')
# password = input('Enter the password: ')
# if len(password) < 8:
#     raise ValueError('To short! At list 8 simvols!')
# elif password.isdigit():
#     raise ValueError('Invalid Password! Only digits!')
# elif password.isalpha():
#     raise ValueError('Invalid Password! Only alphabet!')

# password2 = input('Enter password confirmaion: ')
# if password != password2:
#     raise ValueError('Password didn\'t match!') 
# index = email.find('@')
# print(f'Successfully registered! Hello Mr/Mrs {email[:index]}!')

# age = int(input('Enter your age: '))
# if age.isdigit():
#     age = int(age)
# else:
#     raise ValueError('Invalid value for age!')

# if age < 18:
#     print('Access Denied! Come again after {18 - age} year')
# else: 
#     print('You can buy it!')

# Логические операторы
# and - логические 'и'
# or - логические 'или'
# not - логические 'отрицание'

# money = 1_000_000
# status = 'base'
# if money > 1_000_000 and status == 'premium':
#     print('You\'re president of our club!')
# elif money > 1_000_000 or status == 'premium':
#     print('You\'re minister of our club!')
# else:
#     print('You\'re honorable member of our club!')



















































































