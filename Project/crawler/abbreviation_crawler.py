import json
import os
import requests
from bs4 import BeautifulSoup
import lxml

URL = "https://www.mokhafaf.com/word/%DA%A9%D9%84%D9%85%D8%A7%D8%AA-%D9%81%D8%A7%D8%B1%D8%B3%D9%8A/"
DIR_NAME = '../datasets'
os.makedirs(DIR_NAME, exist_ok=True)

f = requests.get(URL)
soup = BeautifulSoup(f.content, 'lxml')
abbreviations = soup.findAll('div', {'class': 'short-content'})
data = {}
for abbreviation in abbreviations:
    abbreviated = abbreviation.find('h2').getText().replace('مخفف ', '').replace('.', '\u200C')
    real = abbreviation.find('h3').getText()
    data[abbreviated] = real

with open(f"{DIR_NAME}/abbreviation.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False)
