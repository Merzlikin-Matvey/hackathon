# Перед запуском: pip install requests pandas beautifulsoup4 openpyxl
import requests
import pandas as pd
from bs4 import BeautifulSoup as BS

file = open("classification/mcc_codes.txt", "w", encoding="utf-8")
# Запись всех комапаний из исторических данных
try:
    all_organisations = pd.read_excel('../data/clear_data.xlsx')['merchant_name'].unique()
except FileNotFoundError:
    all_organisations = pd.read_excel('data/clear_data.xlsx')['merchant_name'].unique()

file.write(f'ВСЕГО КОМПАНИЙ {len(all_organisations)}\n\n')
progress = 0
for organisation in all_organisations:
    request = requests.get(f'https://mcc-codes.ru/search/?q={'+'.join(organisation.split())}') # Открываем поиск кодов для кампании
    bs = BS(request.content, 'html.parser')
    data = list(bs.findAll("a")) # Ищем все коды
    file.write('\n' + organisation + ':')
    org_types = []
    for i in data:
        if i.text.isdigit(): 
            if len(str(int(i.text))) == 4:
                # Запоминаем тип фирмы
                org_types.append('\n    ' + f'({i.text})' + i['title'])
    # Запись в файл
    if org_types == []: file.write('ДАННЫХ НЕ НАЙДЕННО')
    for type in list(set(org_types)):
        file.write(type)
    progress += 1
    print(f'PROGRESS {progress}/{len(all_organisations)}')

file.close()# Реплит норм тема



