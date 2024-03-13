# 19.01.2023 
# Bolot
# 10 - 12: 
# На лютом хайпе прошли лекцию по циклам (while и for), 
# узнали про оператора моржового типа (:=),
# сразу появился вопрос:  почему не соблезубый тигр или бобр ???
# так же узнали про перенос строки через обратный слеш (\)
# 12 - 18: 
# Закрепление пройденного материала путём решения задач полученных через Telegram

# Циклы - конструкция которая заставляет какой-то блок блога выполнятся несколько раз 

# while <expression>:
#     <body>

# smt = 'default'
# while smt:
#     smt = input('Vvedite chto-to: ')
#     print(smt)

# while smt:= input('Vvedite chto-to: '): #- использование моржового оператора (:=) используется только в циклах
#     print(smt)

# while (smt:= input('Vvedite chto-to: ')) == 'ok': 
    # print(smt)

# i = 1
# while name1 := input('imy1: ') !='John' or \
#     (name2 := input('imy2: ') !='Raychel'):
#     print()

#     if i >= 5:
#         print('Цикл остановлен!')
#         break # принудительная остановка
#     i += 1
# else:
#     print(f'Вы угадали {name1}, {name2}')


# user = {'username':'John_Snow', 'password' : 'bastard123'}
# i = 3
# while password:= input(f'{user["username"]} vvedite parol\': ') != user['password']:
#     i -= 1
#     if i == 0:
#         print('Vy zablokirovany!')
#         break
# else:
#     print(f'{user["username"]} vy uspeshno zashli v sistemu!')

# for <variable> in <iterable object>:
    # <body>

# ls = ['a', 'hello', 55, 66, 77, True]
# i = iter(ls)
# print(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# import random 
# 
# dict_ = {}
# for x in range(1,21):
    # dict_.update({x : random.randint(1, 50)})
# 
# print(dict_)
# 

# ls = ['Tirion', 'Bilal', 'John', 'Sansa', 'Jamie', 'Eddart', ]
# for x in ls:
#     if x.startswith('J'):
#         continue
#     print(f'Hello Mr/Mrs {x}!')





















