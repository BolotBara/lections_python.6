# 'String -> строки'
#  'Hello World! my name is John Snow'

# str1 = '''
# I'm John Snow.
# I'm King of North!
# '''
# print(str1)

# Строки - набор последовательных символов, которые мы используем для хранения и представления текстовой информации

# Индексация в строке
# name = 'John' 
#         # j = 0 = -4
#         # o = 1 = -3
#         # h = 2 = -2
#         # n = 3 = -1
# print(name[1])

# срезы по индексам
# [start: end: <step>]
# str1 = 'birthday'
# print(str1)
# print(str1[0:5])
# print(str1[5:8])
# print(str1[:5])
# print(str1[5:])

# text = 'Hello World! my name is John Snow! I\'m King of North! '
# print(text)
# print(text[:13])
# print(text[:13:2])
# print(text[::2])
# print(text[::-1])

# Конкатенация строк(соединений)
# a = 'hello'
# b = 'world'
# c= ' '
# res = a + ' ' + b
# print(a + b)

# экранирование - способ записи символов в строку, которые невозможно ввести с клавиатуры, либо же запись спец символов которые имеют функционал в питоне

# \n -> перенос строки
# \t -> горизонтальная табуляция
# \v -> вертикальная табуляция
# \' -> апостроф
 
# str1 = "\tHello World!\n\v\tHello John!\n'\\"
# print(str1)

# Форматирование строк
# 1. с помощью %
# 2. с использованиемм .format()
# 3. интерполяция (преоброзование строк) f - stroki

# first_name = input('Vvedite imya:') 
# last_name = input('Vvedite familiyu:') 
# str1 = 'Hello mr/msr %s %s' %(first_name, last_name)
# print(str1)

# first_name = input('Vvedite imya:') 
# last_name = input('Vvedite familiyu:') 
# club = 'Kipish'
# print('Wellcom in da club, {}, mr/msr {} {}!' .format(club, first_name, last_name))

# f - строки
# name = input('Vvedite imya:') 
# last_name = input('Vvedite familiyu:') 
# print(f'Hello mr/msr {name} {last_name}! Wellcom to the party!')

# умножение строк(дублирование)
# str1 = 'Codify'
# print(str1 * 3)
