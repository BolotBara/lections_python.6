# JSON - JavaScript Object Notation
# Единый тесктовый формат данных, был создан для хранения и передачи данных между сервисами, проектами
# <filename>.json # файл в формате JSON
# Процессы Сериализации и Десериализации Данных(конвертация)

# Сериализация (запись данных в JSON) - Это перевод из Python в JSON формат
# dump - записывает данные в файл формата JSON
# dumps - записывает данные в текст формата JSON

# Десериализация (чтение данных из JSON) - это перевод из JSON в Python формат
# load - функция которая считывает данные из файла JSON
# loads - функция которая считывает данные из текста JSON
# import json
# data = {"name": "Ivan", "age": 30, "city": "Moscow"}

# with open("person.json", "w") as file:
#     json.dump(data, file)

# print(data)

# Десериализация (чтение данных из JSON)

# with open("person.json", "r") as file:
#     loaded_data = json.load(file)

# print(loaded_data)

# print(type(loaded_data)) # <class 'dict'>

# Если у вас есть список объектов, то нужно использовать json.loads(), если у вас один объект, то используется json.load().
# print(loaded_data["name"]) # Ivan


# Еще один способ сериализации

# people = [{"name": "Vasya", "age": 25}, {"name": "Petya", "age": 18}]

# with open("people.json", "w") as file:
#     json.dump(people, file, indent=4)  # Добавляет отступы для лучшего вида


# Чтение списка из JSON

# with open("people.json", "r") as file:
#     loaded_people = json.loads(file.read())

# print(loaded_people[0]["name"])  # Vasya


# Обработка ошибок при работе с JSON

# try:
#     with open("not_existing_file.json", "r") as file:
#         content = file.read()
# except FileNotFoundError:
#     print("Файл не найден!")
# else:
#     print("Файл найден.")
# finally:
#     print("В любом случае я выполняюсь.")
# ----------------------------------------------------------------------------------------------------

# процесс сериализации

# import json
# dict_ = {
#     'name': 'John Snow',
#     'age': 24,
#     'status': True,
#     'wife': False,
#     'children': None
# }

# print(dict_, type(dict_))


# import json
# dict_ = {
#     'name': 'John Snow',
#     'age': 24,
#     'status': True,
#     'wife': False,
#     'children': None
# }

# print(dict_, type(dict_))

# with open('new.json', mode='w') as file:   
#     json.dump(dict_, file)

# ----------------------------------------------------------------------------------------------------

# import json

# with open('new.json', 'r') as file:   
#     json_data =  file.read()

# print(json_data, type(json_data))
# dict_ = json.loads(json_data)
# print()
# print(dict_, type(dict_))


# import json

# with open('new.json', 'r') as file:
#     dict_ = json.load(file)
#     print(dict_, type(dict_))
 




