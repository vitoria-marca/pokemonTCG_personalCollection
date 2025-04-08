import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get("https://www.ligapokemon.com.br/?view=cards/search&card=edid=612%20ed=SCR")

time.sleep(2)

buttom = driver.find_element(By.XPATH, '//[@onclick="edc.changeView(2);"]')
buttom.click()

time.sleep(2)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get('https://www.ligapokemon.com.br/?view=cards/search&card=edid=612%20ed=SCR', headers=headers)
content = response.content

ligaPokemon = BeautifulSoup(content, 'html.parser')

#print(type(ligaPokemon))

carta1 = ligaPokemon.find('tr', attrs={'id': 'item=0'})

print(carta1)
#print('Cabeçalho: \n')0
#print(response.content)