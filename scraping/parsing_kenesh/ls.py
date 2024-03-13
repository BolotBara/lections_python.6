from bs4 import BeautifulSoup
import requests
import lxml

url = 'https://softech.kg/phones/Xiaomiphones'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
container = soup.find('div', class_ ='row')
products = container.find_all('div', class_ = 'product-thumb transition')
res = []

for product in products:
    price = product.find('div', class_ = 'price')
    name = product.find('div', class_ = 'name').text
    img = product.find('img', class_ = 'img-responsive').get('data-src')
    description = product.find('div', class_ = 'description-small').text
    data = {'name:': name, 'img' }


