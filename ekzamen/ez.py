# Вы должны спарсить сайт
# https://www.kivano.kg/mobilnye-telefony. Как результат вы должны
# получить:
# 1. Наименование всех телефонов
# 2. Цену каждого продукта(в KGS)
# 3. И ссылка к фотографии
# 4. Все это записать в CSV файл
# Дополнительно(по желанию):
# 1. Ваш парсинг скрипт должен выполняться каждые 60 минут

# Рекомендации:
# 1. BeautifulSoup
# 2. CSV
# 3. lxml
# 3. Requests

# from bs4 import BeautifulSoup
# import requests
# import lxml
# import csv

# def dobavlenie(data):
#     with open('ez.csv', 'a') as file:
#         writer = csv.writer(file)
#         writer.writerow(['№','name','price','img'])
#         number = 1
#         fieldname = ['№','name','price','img']
#         writer = csv.DictWriter(file, fieldname)
#         for product in data:
#             print(product)
#             writer.writerow ({
#             '№': number,
#             'name': product['name'],
#             'price': product['price'],
#             'img': product['img'] 
#             })  
#             number +=1


# url = 'https://www.kivano.kg/mobilnye-telefony'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')
# container = soup.find('div', class_ ='list-view')
# products = container.find_all('div', class_ = 'item product_listbox oh')
# data = []
# counter = 0
# for product in products:
#     counter += 1
#     name = product.find('div', class_ = 'listbox_title oh').text
#     price = product.find('div', class_ = 'listbox_price text-center').text
#     img = product.find('img').get('src')
#     a = 'https://www.kivano.kg'+img
#     phone = {'name': name,'price': price, 'img': a}
#     data.append(phone)

# dobavlenie(data)
