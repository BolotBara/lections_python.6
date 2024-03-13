# 1
from random import randint
num = randint(1, 100)
print(num)
i = 0
while i < 3:
    quess = int(input('Угадай число: '))
    if quess > num:
        print('Горячо', 'поробуйте поменьше')
    if quess < num:
        print('Холодно', 'поробуйте побольше')
    if quess == num: 
        print('Поздравляю ты Гудини!')
        i = 3
    i += 1

# 2
c = 'цельсии'
f = 'форенгейты'
q1 = int(input('Количество градусов которые вы хотите преоброзовать: '))
q2 = (input('Из какого типа желаете преоброзовать: '))
if q2 == c:
    print(q1 * 9/5 + 32) 
if q2 == f:
    print(round((q1 - 32)*5/9, 1)) 

# 3
sum = int(input('Введите сумму кредита: '))
bid = int(input('Введите годовую процентную ставку: '))
term = int(input('На сколько лет был взят кредит: '))
bid1 = bid/12
print(round((sum + (sum * bid1)) / term/12, 1))

# 5
watch = int(input('Введите количество часов: '))
print(watch * 60)

# 6
a = int(input('Введите цену товара: '))
b = int(input('Введите количество товара: '))
print(a * b)

# 7
ear = 365
a = int(input('Введите свой возраст: '))
print(ear * a)

# 8
week = 7
a = int(input('Введите количество дней: '))
print(a // week)
print(a % week)

# 9
from random import choice
a = ('камень', 'ножницы', 'бумага')
b = choice(a)
print(b)
quess = input('Сделайте выбор - камень, ножницы, бумага: ')
if quess == b:
    print('ничья')
if quess == "ножницы" and b == 'камень':
    print('вы проиграли')
if quess == "ножницы" and b == 'бумага':
    print('вы выйграли')
if quess == "камень" and b == 'бумага':
    print('вы проиграли')
if quess == "камень" and b == 'ножницы':
    print('вы выйграли')
if quess == "бумага" and b == 'ножницы':
    print('вы проиграли')
if quess == "бумага" and b == 'камень':
    print('вы выйграли')  







































































































































