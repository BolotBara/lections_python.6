# ТЕХНИЧЕСКОЕ ЗАДАНИЕ(сложность: тяжелая)
# 1. При нажатии на кнопку start, телеграмм бот должен
# зайти на сайт KaktusMedia (https://kaktus.media/) и
# спарсить категорию “Все новости”
# 2. При вводе текста должны выйти первые 20
# заголовков статей с нумерацией. Должна быть
# возможность выбрать новости по нумерации или id
# (по желанию)
# 3. После выбора новости по нумерации, телеграмм
# бот должен отправить сообщение в виде “some
# title news you can see Description of this news
# and Photo” и пользователь отправит текст (либо
# нажмет кнопку) Description, то бот должен
# отправить описание именно текущего поста, также
# аналогично с Photo.
# 4. При нажатии на кнопку «Quit» бот должен
# отправить сообщение “До свидания“

# Рекомендации:
# 1. BeautifulSoup
# 2. CSV
# 3. lxml
# 3. Requests

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup
# import csv
# import time
# import pprint
# import lxml
# # Укажите путь к драйверу Chrome
# chromedriver_path = '/usr/bin/chromedriver'  # Замените на ваш путь к chromedriver
# service = Service(executable_path=chromedriver_path)

# # Настройки для WebDriver
# options = webdriver.ChromeOptions()
# options.headless = False # Установите True, если не нужно открывать окно браузера

# # Переход на страницу
# url = 'https://kaktus.media/?lable=8&date=2024-02-15&order=time'
# def get_html_selenium(url):
#     browser = webdriver.Chrome(service=service, options=options)
#     browser.get(url)

#     # Явные ожидания для загрузки элементов
#     # WebDriverWait(browser, 30).until(
#     #     EC.presence_of_all_elements_located((By.CLASS_NAME, 'card__link'))
#     #     and EC.presence_of_all_elements_located((By.CLASS_NAME, 'main-img'))
#     #     and EC.presence_of_all_elements_located((By.CLASS_NAME, 'price__lower'))
#     #     and EC.presence_of_all_elements_located((By.CLASS_NAME, 'price__discount'))
#     #     and EC.presence_of_all_elements_located((By.CLASS_NAME, 'b-card__name'))
#     #     and EC.presence_of_all_elements_located((By.CLASS_NAME, 'b-card__reviews'))
#     #     and EC.presence_of_all_elements_located((By.CLASS_NAME, 'b-card__rating'))
#     # )
#     time.sleep(2)
#     # Получить HTML-код после выполнения JavaScript
#     html = browser.page_source

#     # Закрыть браузер
#     browser.quit()

#     return html

# def transport_data(html_content):
#     soup = BeautifulSoup(html_content, 'html.parser')

#     product_blocks = soup.find_all('div', class_="ArticleItem--data ArticleItem--data--withImage")
#     # print(product_blocks)
#     result = []
    
#     for block in product_blocks:
#         try: 
#             product_card_title = block.find('a', class_='ArticleItem--name').text.strip()
#         except (AttributeError, TypeError):
#             product_card_title = "Info not found"

#         try: 
#             product_card_desc = block.find('div', class_='ArticleItem--time').text.strip()
#         except (AttributeError, TypeError):
#             product_card_desc = "Desc not found"

#         try:
#             product_personal_link = block.find('a', class_="ArticleItem--name").get('href')
#         except (AttributeError, TypeError):
#             product_personal_link = "Link not found"

#         try:
#             # product_card_img = block.find('data-src', class_='').get('src')
#             img = block.find('img',class_='ArticleItem--image-img ls-is-cached lazyloaded').get('src')
#         except (AttributeError, TypeError):
#             img = "Image not found"
        
#         # info_img= soup_novost.find('div', class_ = 'BbCode').get('src').get('href')
            
#             # info = ' '.join(x.text for x in info_divs)
#             # bio = soup.find('article', class_ = 'clearfix').text.strip().replace('Powered by Froala Editor', '')
#             # img = soup.find('img', class_ ='card-img-top').get('src').replace('', '%20')
#             # write_to_csv(name, info, bio, img, link)
        
#         data = {
#             'title': product_card_title,
#             'desc': product_card_desc,
#             'img': img,
#             'link':product_personal_link,
#             # 'price': product_price,
#             # 'discount': product_price_discount,
#             # 'reviews': product_card_reviews,
#             # 'rating': product_card_rating,
#         }
#         result.append(data)
        

    
#     return result
# # html_content = get_html_selenium(url)
# # data = transport_data(html_content)
# # # print(transport_data(get_html_selenium(url)))

# def kaktus_news_data(link):
#     result_novost = []
#     html = get_html_selenium(link)
#     soup_novost = BeautifulSoup(html, 'html.parser')
#     name = soup_novost.find('h1', class_ = 'Article--title').text.strip()
#     info_divs = soup_novost.find('div', class_ = 'BbCode').text.strip()
#     data_novost = {
#             'name':name,
#             'info':info_divs,
#             # 'img':info_img,
#         }
#     result_novost.append(data_novost)
#     return result_novost


# def excel():
#     with open('kaktus.csv', 'w') as file:
#         fieldname = ['#','title','link', 'desc', 'img',]
#         writer = csv.DictWriter(file, fieldname)
#         writer.writerow({
#             '#': '№','title':'Title','link':'Link','desc':'Desc','img':'Img',
#             })
# excel()
# def excel_news():
#     with open('kaktus_news.csv', 'w') as file:
#         fieldname = ['#','name','info', 'img',]
#         writer = csv.DictWriter(file, fieldname)
#         writer.writerow({
#             '#': '№','name':'Name','info':'Info','img':'Img',
#             })
# excel_news()
# def write_csv(result):
#     count = 1
#     with open('kaktus.csv', 'a') as file:
#         fieldnames = ['#','title','link', 'desc','img']
#         writer = csv.DictWriter(file, fieldnames)
#         writer.writeheader()
#         for transport in result:
#             writer.writerow({
#                 '#': count,
#                 'title':transport['title'],
#                 'link':transport['link'],
#                 'desc':transport['desc'],
#                 'img':transport['img'],   
#             })
#             count +=1
# def write_csv_news(result_news):
#     count = 1
#     with open('kaktus_news.csv', 'a') as file:
#         fieldnames = ['#','name','info','img']
#         writer = csv.DictWriter(file, fieldnames)
#         writer.writeheader()
#         for news in result_news:
#             writer.writerow({
#                 '#': count,
#                 'name':news['name'],
#                 'info':news['info'],
#                 # 'img':news['img'],
                
                
#             })
#             count +=1
# def main():
#     i = 1
#     while i <= 1:  # last_page:
#         page_url = f'https://kaktus.media/?lable=8&date=2024-02-1{i}&order=time'
#         html_content = get_html_selenium(page_url)
#         data = transport_data(html_content)
#         # excel()
#         write_csv(data)
#         print(f'Спарсили {i} pages!')
#         i += 1
#     with open('kaktus.csv','r') as file:
#         csv_reader = csv.DictReader(file)
#         data = [row['Link'] for row in csv_reader]
#         links = data[1:]
#     for link in links:
#         data_news = kaktus_news_data(link)
#         write_csv_news(data_news)
    

#     # kaktus_news_data()

# main()


# # import telebot
# # from telebot import types
# # import random
# # import csv

# # TOKEN="6448618564:AAEKXp8hhl3MMMZNlTanVW_WOY-K9Enqwis"

# # bot = telebot.TeleBot(TOKEN)

# # keyboard = types.ReplyKeyboardMarkup()
# # btn1 = types.KeyboardButton('Yes')
# # btn2 = types.KeyboardButton('No')
# # keyboard.add(btn1,btn2)


# # @bot.message_handler(commands=['start','game'])
# # def start_message(message):
# #     bot_message = bot.send_message(message.chat.id,'Привет Чемпион, начнем игру?', reply_markup=keyboard)
# #     bot.register_next_step_handler(bot_message,check_answer)


# # def check_answer(message):
# #     if message.text == 'Yes':
# #         with open('kaktus.csv','r') as file:
# #             csv_reader = csv.DictReader(file)
# #             data=(row['Title'] for row in csv_reader)
# #             result = ''
# #             # counter = 1
# #             for name in data:
# #                 result += f'{name}\n'
# #                 # counter += 1
# #             # print('123')
# #             # print(result)
# #             st=dict(enumerate(result.split('\n')))
# #     return print(st)


# # # def check_answer(message):
# # #     if message.text == 'Play':
# # #         bot.send_message(message.chat.id, 'Ok, тогда лови правила игры:\nНужно угадать число, которое я загадаю в диапазоне от 1 до 10 вкючительно! У тебя будет 3 попытки! Если не угадаешь я тебя повешу! :)')
# # #         number = random.randint(1,10)
# # #         print(number)
# # #         game(message,3,number)
# # #     elif message.text == 'No,I pass':
# # #         bot.send_message(message.chat.id, 'Нет так нет,Пока!')
# # #     else:
# # #         bot_message = bot.send_message(message.chat.id,'Вы ввели неправильный ответ!',
# # #         reply_markup=keyboard)
# # #         bot.register_next_step_handler(bot_message,check_answer)
# # # def game(message,attempts,number):
# # #     message_bot = bot.send_message(message.chat.id,"Угадай число")
# # #     bot.register_next_step_handler(message_bot,check_number,attempts-1,number)
# # # def check_number(message,attempts,number):
# # #     if message.text == str(number):
# # #         bot.send_message(message.chat.id,'You win')
# # #     elif attempts == 0:
# # #         bot.send_message(message.chat.id,'You dead')
# # #     else:
# # #         bot.send_message(message.chat.id,'No go again churka')
# # #         game(message,attempts,number)
# # bot.polling()#запуск бота
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup
# import csv
# import time
# import pprint
# import lxml
# # Укажите путь к драйверу Chrome
# chromedriver_path = '/usr/bin/chromedriver'  # Замените на ваш путь к chromedriver
# service = Service(executable_path=chromedriver_path)

# options = webdriver.ChromeOptions()
# options.headless = False # Установите True, если не нужно открывать окно браузера


# url = 'https://kaktus.media/?lable=8&date=2024-02-15&order=time'
# def get_html_selenium(url):
#     browser = webdriver.Chrome(service=service, options=options)
#     browser.get(url)

#     # Явные ожидания для загрузки элементов
#     # WebDriverWait(browser, 30).until(
#     #     EC.presence_of_all_elements_located((By.CLASS_NAME, 'card__link'))
#     #     and EC.presence_of_all_elements_located((By.CLASS_NAME, 'main-img'))
#     #     and EC.presence_of_all_elements_located((By.CLASS_NAME, 'price__lower'))
#     #     and EC.presence_of_all_elements_located((By.CLASS_NAME, 'price__discount'))
#     #     and EC.presence_of_all_elements_located((By.CLASS_NAME, 'b-card__name'))
#     #     and EC.presence_of_all_elements_located((By.CLASS_NAME, 'b-card__reviews'))
#     #     and EC.presence_of_all_elements_located((By.CLASS_NAME, 'b-card__rating'))
#     # )
#     time.sleep(2)
#     # Получить HTML-код после выполнения JavaScript
#     html = browser.page_source

#     # Закрыть браузер
#     browser.quit()

#     return html

# def transport_data(html_content):
#     soup = BeautifulSoup(html_content, 'html.parser')

#     product_blocks = soup.find_all('div', class_="ArticleItem--data ArticleItem--data--withImage")
#     # print(product_blocks)
#     result = []
    
#     for block in product_blocks:
#         try: 
#             product_card_title = block.find('a', class_='ArticleItem--name').text.strip()
#         except (AttributeError, TypeError):
#             product_card_title = "Info not found"

#         try: 
#             product_card_desc = block.find('div', class_='ArticleItem--time').text.strip()
#         except (AttributeError, TypeError):
#             product_card_desc = "Desc not found"

#         try:
#             product_personal_link = block.find('a', class_="ArticleItem--name").get('href')
#         except (AttributeError, TypeError):
#             product_personal_link = "Link not found"

#         try:
#             # product_card_img = block.find('data-src', class_='').get('src')
#             img = block.find('img',class_='ArticleItem--image-img ls-is-cached lazyloaded').get('src')
#         except (AttributeError, TypeError):
#             img = "Image not found"
        
#         # info_img= soup_novost.find('div', class_ = 'BbCode').get('src').get('href')
            
#             # info = ' '.join(x.text for x in info_divs)
#             # bio = soup.find('article', class_ = 'clearfix').text.strip().replace('Powered by Froala Editor', '')
#             # img = soup.find('img', class_ ='card-img-top').get('src').replace('', '%20')
#             # write_to_csv(name, info, bio, img, link)
        
#         data = {
#             'title': product_card_title,
#             'desc': product_card_desc,
#             'img': img,
#             'link':product_personal_link,
#             # 'price': product_price,
#             # 'discount': product_price_discount,
#             # 'reviews': product_card_reviews,
#             # 'rating': product_card_rating,
#         }
#         result.append(data)
        

    
#     return result
# # html_content = get_html_selenium(url)
# # data = transport_data(html_content)
# # # print(transport_data(get_html_selenium(url)))

# def kaktus_news_data(link):
#     result_novost = []
#     html = get_html_selenium(link)
#     soup_novost = BeautifulSoup(html, 'html.parser')
#     name = soup_novost.find('h1', class_ = 'Article--title').text.strip()
#     info_divs = soup_novost.find('div', class_ = 'BbCode').text.strip()
#     data_novost = {
#             'name':name,
#             'info':info_divs,
#             # 'img':info_img,
#         }
#     result_novost.append(data_novost)
#     return result_novost


# def excel():
#     with open('kaktus.csv', 'w') as file:
#         fieldname = ['#','title','link', 'desc', 'img',]
#         writer = csv.DictWriter(file, fieldname)
#         writer.writerow({
#             '#': '№','title':'Title','link':'Link','desc':'Desc','img':'Img',
#             })
# excel()
# def excel_news():
#     with open('kaktus_news.csv', 'w') as file:
#         fieldname = ['#','name','info', 'img',]
#         writer = csv.DictWriter(file, fieldname)
#         writer.writerow({
#             '#': '№','name':'Name','info':'Info','img':'Img',
#             })
# excel_news()
# def write_csv(result):
#     count = 1
#     with open('kaktus.csv', 'a') as file:
#         fieldnames = ['#','title','link', 'desc','img']
#         writer = csv.DictWriter(file, fieldnames)
#         writer.writeheader()
#         for transport in result:
#             writer.writerow({
#                 '#': count,
#                 'title':transport['title'],
#                 'link':transport['link'],
#                 'desc':transport['desc'],
#                 'img':transport['img'],       
#             })
#             count +=1
# def write_csv_news(result_news):
#     count = 1
#     with open('kaktus_news.csv', 'a') as file:
#         fieldnames = ['#','name','info','img']
#         writer = csv.DictWriter(file, fieldnames)
#         writer.writeheader()
#         for news in result_news:
#             writer.writerow({
#                 '#': count,
#                 'name':news['name'],
#                 'info':news['info'],
#                 # 'img':news['img'],
#             })
#             count +=1
# def main():
#     i = 1
#     while i <= 1:  # last_page:
#         page_url = f'https://kaktus.media/?lable=8&date=2024-02-1{i}&order=time'
#         html_content = get_html_selenium(page_url)
#         data = transport_data(html_content)
#         # excel()
#         write_csv(data)
#         print(f'Спарсили {i} pages!')
#         i += 1
#     with open('kaktus.csv','r') as file:
#         csv_reader = csv.DictReader(file)
#         data = [row['Link'] for row in csv_reader]
#         links = data[1:]
#     for link in links:
#         data_news = kaktus_news_data(link)
#         write_csv_news(data_news)

#     # kaktus_news_data()
