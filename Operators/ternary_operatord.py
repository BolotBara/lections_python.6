# sentence = input('Vvedite predlojeniye:')
# if sentence[-1] =='?':
#     print('Yes voprositel\'noye!')
# else:
#     print('Normal one')

# sentence = input('Vvedite predlojeniye:')
# res = 'Yes voprositel\'noye!' if sentence[-1] =='?' else 'Normal one'
# print(res)

# тернарый оператор(Ternary operators) - это конструкция которая по своему действию аналогична конструкции
# if/else, но при этом записывается в одну строчку

# num = int(input('Vvedite chislo: '))
# print('even num' if num % 2 == 0 else 'odd number')

# ls = [45,45,45,4,54,85,95]
# guess = input('Вывести максимальное или минимальное значение: ')
# res = max(ls) if guess == 'max' else min(ls) if guess == 'min' else 'Invalid operator!'
# print(res)
# if guess == 'max':
#     print(max(ls))
# else:
#     print(min(ls))

# -----------------------------------------------------------
# flag = True
# symbols = '0123456789' + '-' + '.'
# while flag:
#     num1 = input('Number 1:')
#     is_corrent_num = True
#     for x in num1:
#         if x not in symbols:
#             print('Вы ввели некоректное число!')
#             is_corrent_num = False
#             break
#     if not is_corrent_num:
#         continue
#     num2 = input('Number 2:')
#     is_corrent_num = True
#     for x in num2:
#         if x not in symbols:
#             print('Вы ввели некоректное число!')
#             is_corrent_num = False
#             break
#     if not is_corrent_num:
#         continue

#     num1 = float(num1) if '.' in num1 else int(num1)
#     num2 = float(num2) if '.' in num2 else int(num2)

#     print(num1, type(num1))
#     print(num2, type(num2))
    
#     operator = input('Введите операцию(+,-,*,/): ').strip()
#     if operator == '+':
#         print(f'Результат: {num1 + num2}')
#     elif operator == '-':
#         print(f'Результат: {num1 - num2}')
#     elif operator == '*':
#         print(f'Результат: {num1 * num2}')
#     elif operator == '/':
#         print(f'Результат: {num1 / num2}') if num2 != 0 else 'Na nol ne deli'
#     else:
#         print('Вы ввели неверный оператор!')
#     choice = input('Хотите продолжить работу (yes\no)?:')
#     if choice.lower().strip() != 'yes':
#         flag = False
#         print('Пока пока!')


































