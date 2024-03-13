# ТЕХНИЧЕСКОЕ ЗАДАНИЕ(сложность: средняя)
# ● Спарсить kolesa.kz, категорию:
# 1.Название всех моделей.
# 2.Цену всех моделей
# 3.Изображение всех моделей
# 4.Краткое описание всех моделей
# 5.Записать все в csv файл

# Рекомендации:
# 1. BeautifulSoup
# 2. CSV
# 3. lxml
# 3. Requests

from bs4 import BeautifulSoup
import requests
import lxml
import csv

def dobavlenie(data):
    with open('medium.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(['№','name','price','img','tip'])
        number = 1
        fieldname = ['№','name','price','img','tip']
        writer = csv.DictWriter(file, fieldname)
        for product in data:
            print(product)
            writer.writerow ({
            '№': number,
            'name': product['name'],
            'price': product['price'],
            'img': product['img'],
            'tip': product ['tip']
            })  
            number +=1


url = 'https://auto312.kg/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
container = soup.find('div', class_ ='dj-items-rows')
products = container.find_all('div', class_ = 'item_row_in')
data = []
counter = 0
for product in products:
    counter += 1
    name = product.find('div', class_ = 'item_title').text
    price = product.find('div', class_ = 'item_price').text
    img = product.find('img').get('src')
    a = 'https://auto312.kg/'+img
    opisanie = product.find('div', class_ = 'item_custom_fields').text
    car = {'name': name,'price': price, 'img': a, 'tip': opisanie}
    data.append(car)

dobavlenie(data)

