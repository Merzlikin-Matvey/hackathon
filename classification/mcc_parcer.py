#Перед запуском: pip install requests pandas beautifulsoup4 openpyxl
import requests
import pandas as pd
from bs4 import BeautifulSoup as BS

request = requests.get(f'https://mcc-codes.ru/search/?q={'KFC'}')
bs = BS(request.content, 'html.parser')

try:
    all_organisations = pd.read_excel('../data/clear_data.xlsx')['merchant_name'].unique()
except:
    all_organisations = pd.read_excel('data/clear_data.xlsx')['merchant_name'].unique()


print(all_organisations)
data = list(bs.findAll("a"))
for i in data:

    if i.text.isdigit(): 
        print(i.text)
        try:
            print(i['data-original-title'])
        except:
            100

