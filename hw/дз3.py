# 1) Палиндром:
# Напишите программу, которая проверяет, является ли введенная пользователем строка палиндромом (читается одинаково с начала и с конца, игнорируя пробелы, регистр букв).
a = 'ana    ana   '
b = a.lower().replace(' ', '')
c = b == b[::-1]
print(c, a, sep= '\n')


# 2) Подсчет слов:
# Программа должна принимать текст и слово. Напишите программу, которая подсчитывает количество слов в этом предложении.
s = "Это биба"
words = s.split()
num_words = len(words)
print(num_words)

# 3) Генерация пароля:
# Напишите программу, которая генерирует случайный пароль заданной длины. Пароль должен содержать как буквы, так и цифры.
import random
import string
length = 10
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print(password)


# 4) Поиск повторяющихся символов:
# Напишите программу, которая проверяет, есть ли в веденной строке повторяющиеся символы.
word = input('Введите слово: ')
for i in range(len(word)):
    if word[i] not in word[:i]:
        print(word[i], word.count(word[i]))

    

# 5) Подсчет гласных и согласных:
# Введите строку, а затем напишите программу, которая подсчитывает количество гласных и согласных букв в ней.
# Ввод строки от пользователя
input_string = 'bolotbek'
input_string = input_string.lower()

vowel_count = 0
consonant_count = 0

vowels = "aeiouаеёиоуыэюя"
consonants = "bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщ"

for char in input_string:
    if char in vowels:
        vowel_count += 1
    elif char in consonants:
        consonant_count += 1

print(f"Количество гласных букв: {vowel_count}")
print(f"Количество согласных букв: {consonant_count}")










