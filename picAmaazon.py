import time
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By # queda pendiente
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

response = requests.get("https://www.amazon.com.mx/ref=nav_logo")
print(response.status_code)

s = Service(ChromeDriverManager().install())
opc = Options()
opc.add_argument("--window-size= 1020, 1200")

navegador = webdriver.Chrome(service=s, options=opc)
navegador.get("https://www.amazon.com.mx/ref=nav_logo")

soup = BeautifulSoup(navegador.page_source, "html.parser")

product = input("Que producto desea buscar? ")

searchBox = navegador.find_element(By.NAME, "field-keywords")
searchBox.send_keys(product)
searchBox.submit()
time.sleep(5)

navegador.save_screenshot("picAmazon.png")