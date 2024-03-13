# 1) Часы и минуты в секунды: Напишите функцию, которая принимает целочисленные значения часов и минут, конвертирует эти значения в секунды, а затем суммирует их и возвращает в качестве результата.

def my_time(hour, min) -> int:
    """
    This function takes two integers as input: hour and minute. It returns a string that represents the time in hours and minutes."""
    return hour*60*60 + min*60

print(my_time(10, 10))
# 2) Возраст в дни: Напишите функцию, которая принимает возраст (количество лет) и преобразует это значение в количество дней.
def my_age(age) -> int:
    day_in_year = 365
    return day_in_year * age
    

print(my_age(20))

# 3) Сколько ног на ферме: Для решения этой задачи необходимо написать функцию, которая посчитает количество ног у всех животных на ферме. На ферме живут курочки, коровки, и свинки. Зная количество животных каждого вида, посчитайте, сколько всего ног у всех животных на ферме.

def legs(animal):
    count_leg = 0
    for i in animal:
        count_leg += animal[i]
    return count_leg


animal_dict = {'chiken': 2, 'cow': 4, 'pig': 4}
print(legs(animal_dict))