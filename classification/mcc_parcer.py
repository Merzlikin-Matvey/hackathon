import requests
from bs4 import BeautifulSoup as BS

request = requests.get(f'https://mcc-codes.ru/search/?q={'KFC'}')
bs = BS(request.content, 'html.parser')


