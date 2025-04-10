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

ligaPokemon = BeautifulSoup(browser.page_source, 'html.parser')

cards = ligaPokemon.select("tr[id^='item_']") 

for card in cards:
    cells = card.find_all("td")

    card_number = cells[0].get_text()
    card_name = cells[1].get_text()
    card_type = cells[2].get_text()
    min_value = cells[4].get_text()
    max_value = cells[5].get_text()
    
    print(f"Carta: {card_name} | Nº: {card_number} | Tipo: {card_type} | Min: {min_value} | Max: {max_value}")
