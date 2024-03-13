# # Задание 1 (15 баллов)

# # Даны списки:
# # a = [1, 1, 2.3, 3, -5, 8, -13, -21, 34.5, 55, 89];
# # b = [1, 2.3, 3, 4, -5, 6, 7, 8, 9, -10, 11, -12, -13, 34.5].
# # Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
# # Продолжите работать с этим списком:
# # Используя функции и методы которые прошли на уроке:
# # Все отрицательные числа "вырезать" и вставить в новый список negative_list, не изменяя основной (общий) список и распечатать список negative_list
# # Всем отрицательным числам  в списке negative_list вернуть абсолютное значение
# # Возвести в степень 3, первый и последний элементы в общем списке

# # a = [1, 1, 2.3, 3, -5, 8, -13, -21, 34.5, 55, 89]
# # b = [1, 2.3, 3, 4, -5, 6, 7, 8, 9, -10, 11, -12, -13, 34.5]
# # new_list = []
# # for i in a:
# #     if i in b:
# #         new_list.append(i)
# # negative_list = []
# # for i in new_list:
# #     if i < 0:
# #         negative_list.append(abs(i))     

# # new_list = set(new_list)
# # new_list = list(new_list)
# # print(new_list)
# # print(negative_list)
# # print(pow(new_list[0], 3), pow(new_list[-1], 3))

# # Задание 2 (40 баллов)

# # Во многих странах существует традиция помещать портреты своих бывших политических лидеров или других выдающихся личностей на банкноты. Ниже приведены номиналы банкнот Кыргызстана с изображенными на них людьми.
# # Banknote = [‘Абдылас Малдыбаев’, ‘Бубусара Бейшеналиева’, ‘Касым Тыныстанов’, ‘Тоголок Молдо’, ‘Курманджан Датка’,  ‘Бенджамин Франклин’]

# # Абдылас Малдыбаев 1 сом
# # Бубусара Бейшеналиева 5 сом
# # Касым Тыныстанов 10 сом
# # Тоголок Молдо 20 сом
# # Курманджан Датка 50 сом
# # Токтогул Сатылганов 100 сом

# # Необходимо написать код, который:
# # В списке указан Франклин, портрет которого не используется в банкнотах Кыргызстана, значит нужно заменить его на Токтогула Сатылганова.
# # Также в списке отсутствуют известные люди, портреты которых размещены на купюрах достоинством 200 сом, 500сом, 1000 сом. Необходимо их добавить.
# # Напишите программу, которая будет запрашивать у пользователя номинал банкноты и отображать на экране имя деятеля, портрет которого размещен на соответствующем денежном знаке.
# # Для того чтобы отобразить имя, чей портрет на банкноте, необходимо воспользоваться выводом элемента из списка по индексу.
# # Если банкноты введенного номинала не существует, должно выводиться сообщение об ошибке.

# banknote_dict = {
#     1: 'Abdylas Maldybaev',
#     5: 'Bubusara Beishenalieva',
#     10: 'Kasym Tynystanov',
#     20: 'Togolok Moldo',
#     50: 'Kurmanjan Datka',
#     100: 'Toktogul Satylganov',  
#     200: 'New Figure for 200 som', 
#     500: 'New Figure for 500 som',  
#     1000: 'New Figure for 1000 som'  
# }
# banknote_dict[1] = 'Toktogul Satylganov'
# denomination = int(input("Enter the denomination of the banknote: "))
# try:
#     figure_name = banknote_dict[denomination]
#     print(f"The figure on the {denomination} som banknote is: {figure_name}")
# except KeyError:
#     print("Error: This denomination does not exist.")

# # Задача 3. (10 баллов)

# # В ресторане меню бизнес-ланча зависит от дня недели. На кухне у поваров на всякий случай висит табло, на котором отображается день недели и сколько часов уже отработано. Ну, чтобы не забыть, мало ли. А ещё пятница — день хороший, поэтому можно даже уходить пораньше.
# # Напишите программу: пользователь вводит номер дня недели от 1 до 7 и количество отработанных часов рабочего дня (0...8). Программа выводит на экран день недели текстом (понедельник, вторник и так далее). В пятницу пропишите дополнительную проверку: если до конца рабочего дня меньше двух часов, то нужно вывести сообщение «Можно уйти пораньше!».

# # Пример 1:
# # Введите номер дня недели: 4
# # Введите количество отработанных часов: 6
# # Сегодня четверг.
# # Осталось работать 2 часа

# # Пример 2:
# # Введите номер дня недели: 5
# # Введите количество отработанных часов: 7
# # Сегодня пятница.
# # Осталось работать 1 час
# # Можно уйти пораньше!

# def get_day_name(day_number):
#     days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#     return days[day_number - 1]
# day_number = int(input("Enter the day of the week number (1-7): "))
# hours_worked = int(input("Enter the number of hours worked (0-8): "))
# if 1 <= day_number <= 7 and 0 <= hours_worked <= 8:
#     day_name = get_day_name(day_number)
#     remaining_hours = 8 - hours_worked
#     if day_number == 5 and remaining_hours < 2:
#         print(f"Today is {day_name}.")
#         print(f"There is {remaining_hours} hour left to work.")
#         print("You can leave early!")
#     else:
#         print(f"Today is {day_name}.")
#         print(f"There are {remaining_hours} hours left to work.")
# else:
#     print("Invalid input. Please enter valid values.")

# # Задача 4. (10 баллов)
# # Мы участвуем в разработке приложения для математиков, где можно будет делать всё, начиная от простейших вычислений и заканчивая построением сложных графиков. В этом приложении реализована установка диапазона чисел, и нам необходимо написать этакую «защиту от дурака».
# # Напишите программу, которая получает на вход число и проверяет, двузначное оно или нет. Выведите соответствующее сообщение.

# number = int(input("Enter a number: "))
# if 10 <= number <= 99:
#     print("The number is two-digit.")
# else:
#     print("The number is not two-digit.")

# # Задача 5. (10 баллов)

# # Папа-программист уже настолько обленился, что вместо того, чтобы самому спросить у сына, какую оценку тот получил в школе, он написал для этого вот такую программу:
# # rating = int(input('Что получил по математике? '))
# # if rating == 2:
# #  print('Плохо. Марш учиться!')
# # if rating == 3:
# #  print('Плохо. Марш учиться!')
# # if rating == 4:
# #  print('Молодец! Можешь отдохнуть.')
# # if rating == 5:
# #  print('Молодец! Можешь отдохнуть.')
# # Сын после того, как «сообщил» свою оценку, посмотрел на код программы и понял, что её можно улучшить, и даже рассказал папе, как это сделать, за что получил безграничное уважение от отца.
# # Скопируйте программу в редактор и оптимизируйте:
# # При плохой оценке (2 или 3) выводится сообщение: «Плохо. Марш учиться!».
# # При хорошей оценке (4 или 5) выводится сообщение: «Молодец! Можешь отдохнуть».
# # В программе не должно быть повторяющихся строк.

# rating = int(input('What did you get in math? '))
# if rating == 2 or rating == 3:
#     print('Bad. March to study!')
# elif rating == 4 or rating == 5:
#     print('Well done! You can rest now.')

# # Задача №6 (15 баллов)

# # Найдите сумму всех элементов списка [1, '2', 3, 4, '5'', ''шесть", "семь"], предварительно приводя строки к целым числам и заменяя буквенные значения на числа; выведите ответ на экран; создайте 2 списка с четными и нечетными числами и выведите их на экран

# sum_list = [1, '2', 3, 4, '5', 'шесть', 'семь']
# u = 0
# for i in sum_list:
#     sum_list[sum_list.index(i)] = (sum_list.index(i)+1)
# print(sum(sum_list))
# print(sum_list)
# even_num = []
# odd_num = []
# for i in sum_list:
#     if i % 2 == 0:
#         even_num.append(i)
#     else:
#         odd_num.append(i)
# print(even_num, odd_num, sep='\n')


