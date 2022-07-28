from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import os

PATH = os.getcwd()
XSS_URL = 'http://127.0.0.1:8000/accueil/1'
COOKIES = {'name': 'ADMIN_TOKEN', 'value': 'T3LeC0oK_5uP3R_Co0K1e!!!'}


os.environ['PATH'] = os.environ['PATH'] + ':' + PATH

options = Options()
options.headless = False
driver = webdriver.Firefox(options=options)

driver.get(XSS_URL)
driver.add_cookie(COOKIES)
driver.refresh()

nb_messages = len(driver.find_elements(By.CLASS_NAME, "message")) - 1

for i in range(nb_messages):
    driver.find_elements(By.CLASS_NAME, "message")[0].click()
    driver.get(XSS_URL + "?delete=YesIAmTheBotYouCanDeleteLastMessage!!:)")