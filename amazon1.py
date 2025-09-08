import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

response = requests.get("https://www.amazon.com.mx/ref=nav_logo")


s = Service(ChromeDriverManager().install())
opc = Options()
opc.add_argument("--window-size=1020,1200")

navegador = webdriver.Chrome(service=s, options=opc)
navegador.get("https://www.amazon.com.mx/ref=nav_logo")

product = input("¿Qué producto desea buscar? ")
num = 5

searchBox = navegador.find_element(By.NAME, "field-keywords")
searchBox.send_keys(product)
searchBox.submit()

datos = {"Nombre": [], "Ratings": [], "Precio": [], "Fecha": []}

for page in range(1, num + 1):
    time.sleep(2)
    soup = BeautifulSoup(navegador.page_source, "html.parser")
    listaDivs = soup.find_all("div", attrs={"a-section a-spacing-small puis-padding-left-small puis-padding-right-small"})

    for div in listaDivs:
        Nombre = div.find("h2", attrs={"class": "a-size-mini a-spacing-none a-color-base s-line-clamp-4"})
        Ratings = div.find("i", attrs={"class": "a-icon a-icon-star-small a-star-small-4-5 aok-align-bottom"})
        Precio = div.find("span", attrs={"class": "a-price-whole"})
        Fecha = div.find("span", attrs={"class": "a-color-base a-text-bold"})

        rating_text = Ratings.text if Ratings else ""
        rating = rating_text.split(" ")[0]

        datos["Nombre"].append(Nombre.text.strip() if Nombre else "")
        datos["Ratings"].append(rating)
        datos["Precio"].append(Precio.text.strip() if Precio else "")
        datos["Fecha"].append(Fecha.text.strip() if Fecha else "")

    if page < num:
        nextPage = navegador.find_element(By.CSS_SELECTOR, "a.s-pagination-item.s-pagination-next.s-pagination-button")
        nextPage.click()
    else:
        break

dataDf = pd.DataFrame(datos)

print(dataDf)
dataDf.to_csv("amazon.csv")

