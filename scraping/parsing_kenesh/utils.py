from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains


chromedriver_path = '/usr/bin/chromedriver'  # Замените на ваш путь к chromedriver
service = Service(executable_path=chromedriver_path)

chrome_options = webdriver.ChromeOptions()

def get_deps_html_selenium(url):
    driver = webdriver.Chrome(service=service,options=chrome_options)
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'card-title')))
    html = driver.page_source
    driver.quit() 
    return html



def get_page_html_selenium(url):
    driver = webdriver.Chrome(service=service,options=chrome_options)
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'section-footer')))
    
    i=1
    res= {}
    while i <= 8:
        sleep(1)
        html = driver.page_source
        res[i]=html
        sleep(1)
        page_button = driver.find_elements(By.CSS_SELECTOR, '.page-link')

        element = page_button[-1]
        
        
        if page_button:
            ActionChains(driver).move_to_element(element).perform()
            sleep(1)
            element.click()

        i +=1
    

    driver.quit() 
    return res
