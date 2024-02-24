# Перед запуском: pip install requests pandas beautifulsoup4 openpyxl

import json
import requests
import pandas as pd
from bs4 import BeautifulSoup as BS

file = open("classification/mcc_codes.json", "w", encoding="utf-8")
# Запись всех комапаний из исторических данных
try:
    all_organisations = pd.read_excel('../data/clear_data.xlsx')['merchant_name'].unique()
except FileNotFoundError:
    all_organisations = pd.read_excel('data/clear_data.xlsx')['merchant_name'].unique()

progress = 0
data = {"count": len(all_organisations)}
for organisation in all_organisations:
    request = requests.get(f'https://mcc-codes.ru/search/?q={'+'.join(organisation.split())}') # Открываем поиск кодов для кампании
    bs = BS(request.content, 'html.parser')
    objects = list(bs.findAll("a")) # Ищем все коды
    org_types = []
    mcc_codes = []
    for i in objects:
        if i.text.isdigit(): 
            if len(str(int(i.text))) == 4:
                # Запоминаем тип фирмы
                org_types.append(i['title'])
                mcc_codes.append(i.text)
    # Запись в файл
    if org_types == []: data[organisation] = None
    else: data[organisation] = [max(org_types, key= lambda x: org_types.count(x)), max(mcc_codes, key= lambda x: mcc_codes.count(x))]
    progress += 1
    print(f'PROGRESS {progress}/{len(all_organisations)}')

json.dump(data, file, indent=4, ensure_ascii=False)
file.close()# Реплит норм тема


# Функция для получения типа фирмы
# На выходе список из типа фирмы и его mcc код или None если типа фирмы не найдено
def Get_type(org_name: str):# На вход подается название
    request = requests.get(f'https://mcc-codes.ru/search/?q={'+'.join(org_name.split())}') # Открываем поиск кодов для кампании
    bs = BS(request.content, 'html.parser')
    objects = list(bs.findAll("a")) # Ищем все коды
    org_types = []
    mcc_codes = []
    for i in objects:
        if i.text.isdigit(): 
            if len(str(int(i.text))) == 4:
                # Запоминаем тип фирмы
                org_types.append(i['title'])
                mcc_codes.append(i.text)
    # Запись в файл
    if org_types == []: return None
    else: return [max(org_types, key= lambda x: org_types.count(x)), max(mcc_codes, key= lambda x: mcc_codes.count(x))]
