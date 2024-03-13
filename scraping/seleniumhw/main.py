# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import csv
# import time

# chromedriver_path = '/usr/bin/chromedriver'
# service = Service(executable_path=chromedriver_path)
# options = webdriver.ChromeOptions()
# options.headless = False
# browser = webdriver.Chrome(service=service, options=options)

# def write_to_csv(file_path, data):
#     with open(file_path, 'a', newline='', encoding='utf-8') as file:
#         fieldnames = ['#', 'title', 'price', 'discount', 'img', 'reviews', 'rating']
#         writer = csv.DictWriter(file, fieldnames=fieldnames)
#         if file.tell() == 0:  
#             writer.writeheader()
#         for index, laptop in enumerate(data, start=1):
#             writer.writerow({
#                 '#': index,
#                 'title': laptop.get('title', 'Title not found'),
#                 'price': laptop.get('price', 'Price not found'),
#                 'discount': laptop.get('discount', 'Discount not found'),
#                 'img': laptop.get('img', 'Image not found'),
#                 'reviews': laptop.get('reviews', 'Reviews not found'),
#                 'rating': laptop.get('rating', 'Rating not found')
#             })

# def parse_page():
#     result = []
#     product_blocks = browser.find_elements(By.CLASS_NAME, 'card__link')
#     for block in product_blocks:
#         try:
#             product_card_picture = block.find_element(By.CLASS_NAME, 'main-img').get_attribute('src')
#         except:
#             product_card_picture = "Image not found"

#         try:
#             product_price_lower = block.find_element(By.CLASS_NAME, 'price__lower').text
#         except:
#             product_price_lower = "Price not found"

#         try:
#             product_price_discount = block.find_element(By.CLASS_NAME, 'price__discount').text
#         except:
#             product_price_discount = "Discount not found"

#         try:
#             product_card_brand = block.find_element(By.CLASS_NAME, 'b-card__name').text
#         except:
#             product_card_brand = "Brand not found"

#         try:
#             product_card_reviews = block.find_element(By.CLASS_NAME, 'b-card__reviews').text
#         except:
#             product_card_reviews = "Reviews not found"

#         try:
#             product_card_rating = block.find_element(By.CLASS_NAME, 'b-card__rating').text
#         except:
#             product_card_rating = "Rating not found"

#         data = {
#             'img': product_card_picture,
#             'title': product_card_brand,
#             'price': product_price_lower,
#             'discount': product_price_discount,
#             'reviews': product_card_reviews,
#             'rating': product_card_rating,
#         }
#         result.append(data)
#     return result

# def scrape_pages(num_pages):
#     for i in range(1, num_pages + 1):
#         page_url = f'https://global.wildberries.ru/catalog?category=9492&page={i}'
#         browser.get(page_url)
#         time.sleep(5)  
#         data = parse_page()
#         write_to_csv('WB.csv', data)
#         print(f'Scraped page {i}/{num_pages}')
#     browser.quit()

# scrape_pages(10)
