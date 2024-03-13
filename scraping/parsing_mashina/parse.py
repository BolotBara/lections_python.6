from bs4 import BeautifulSoup 
import requests
import csv
import pprint

url = 'https://www.mashina.kg/search/all/'

def parsing_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    container = soup.find('div', class_ = 'table-view-list')
    cars = container.find_all('div', class_ = 'list-item')
    result = []
    for car in cars:
        name = car.find('h2', class_ = 'name').text.strip()
        try:
            img = car.find('img', class_ = 'lazy-image-attr').get('src')
        except Exception as e:
            img = f'No image, {e}!'
        price = car.find('div', class_ = 'block price').find('strong').text
        description = ''.join(car.find('div', class_='block info-wrapper item-info-wrapper').text.split())
        data = {'title': name, 'description': description, 'price': price, 'img': img}
        result.append(data)
    return result


def get_last_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    pages = soup.find_all('a', class_='page-link')[-1]
    print(pages)
    return int(pages.get('data-page'))


def prepare_csv():
    with open('cars.csv', 'w') as file:
        fieldname = ['№', 'name', 'decription', 'price', 'img']
        writer = csv.DictWriter(file, fieldname)
        writer.writerow({
            '№': '№',
            'name': 'Name',
            'decription': 'Decription',
            'price': 'Price: ',
            'img': 'Image URL' #
        })


def write_to_csv(data: list):
    with open('cars.csv', 'a') as file:
        global count
        fieldname = ['№', 'name', 'decription', 'price', 'img']
        writer = csv.DictWriter(file, fieldname)
        for car in data:
            writer.writerow ({
            '№': count,
            'name': car['title'],
            'decription': car['description'],
            'price': car['price'],
            'img': car['img'] 
            })  
            count +=1

prepare_csv()
url = f'https://www.mashina.kg/search/all'
last_page = get_last_page(url)
print(last_page)
count = 1
i = 1
while i<= last_page:
    page_url = f'https://www.mashina.kg/search/all/?page=2{i}'
    data = parsing_data(page_url)
    write_to_csv(data)
    print(f'Спарсили{i}/{last_page} страницу!')
    i+=1
data = parsing_data(url)
write_to_csv(data)

#SELENIUM - parsing