import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time

options = Options()
#options.add_argument('--headless') não aparece o navegador enquanto o script roda
options.add_argument('window-size=1200,800')

browser = webdriver.Edge(options=options)
browser.get('https://www.ligapokemon.com.br/?view=cards/search&card=edid=612%20ed=SCR')

time.sleep(2)

button = browser.find_element(By.CLASS_NAME, 'white-list-img')
button.click()

time.sleep(2)
#ligaPokemon = BeautifulSoup(browser.page_source, 'html.parser')

#print(ligaPokemon.prettify())