# text = 'The more you learn, the more you earn.'
# len() - возвращает длину строbки считая каждый ее символ
# len_text = len(text)
# print(len_text) 
# print(text[5:6:])
# print(text[::-1])

# count_e = 0
# i = 0
# while i < len_text:
#     symbol = text[i]
#     if symbol == 'e' or symbol =='E':
#         count_e += 1
#     print(symbol)
#     i += 1

# print(f'Symbol E is found: {count_e} times!1')

# custom len code
# text = 'The more you learn, the more you earn.'

# i = 0

# while text[i:]:
#     i += 1
   
# print(i)

# ------------------------------------------------

# Методы строк - dir()
# print(dir("123"))

# Методы строк
# text1 = 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 
# 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal',
# 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle',
# 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 
# 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit','rstrip', 
# 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'   

# count(value, [start]) - считает кол-во вхождений value в нашу строку
# text = "hello o o o o hello"
# print(text1.count( ))

# replace(old, new, [count]) - меняет в строке old символ на new, заменит count  раз если передаете число
# text = ' ha h hah hah hah ah ah ah ah ah a ha ha ah ahaaha h ah ah its time Joker'
# res = text.replace('a','e', 4)
# print(f'original text: {text}')
# print(f'NOT original text: {res}')

# strip() - Убирает пробельные символы в начале и в конце строки
# rstrip, lstrip
# a = '   Hello   '
# print(a ,len(a), sep='->')
# res = a.strip()
# print(res, len(res), sep='->')
# print(a.lstrip(), '1')

# isdigit -         ПРОВЕРЯЕТ
# isnumeric - состоит ли наша строка
# isdecimal -   полностью из чисел

# num = input('Write number: ')
# print(f'Wrote li number?: {num.isdigit()}')

# isalpha - состоит ли наша строка из символов алфавита
# print('Helloworld'.isalpha())

# isalnum - состоит ли наша строка из символов алфавита
# txt = 'Hello World'
# print(txt.isalpha())
# res = txt.replace(' ', '')
# print(res, res.isalpha())

# num = input('Vvedite chislo:')
# if num.isdigit():
#     num = int(num)
#     print(f'{num} * 5 = {num * 5}')
# else:
#     print('Vy vveki ne chislo!')

# split(separator) - дробит(дробит) сроку на несколько частей по разделителю, все части сохраняются в типе list

# text = 'Let me speak in English'
# res = text.split('e')
# print(text)
# print(res)
# print(text.split)

# a = '#hello#life#work#love#bishkek'
# pint(a)
# print(a[l:].split('#'))

# 'connector'.join(list) - соединяет по connector строки которые были в list
# ls = ['Anvar', 'john', 'Jamie', 'Osmon']
# print(ls)
# res = '-'.join(ls)
# print(res)

# swapcase() - переводит все символы в противоположный регистр
# upper() - переводит все в верхний регистр
# lower() - переводит все в нижний регистр

# text = 'Hello world, JOHN Snow'
# print(f'Original: {text}')
# print(text.swapcase())
# print(text.upper())
# print(text.lower())

# index(value) - находит индекс значения value внутри строки
# find(value) - делает тоже самое что и index, но если не нашел value то вернется -1

# text = 'hello John Snow'
# print(text.index('o'))
# print(text.index('John'))
# print(text.index('o', 5))
# print(text.find('a'))



