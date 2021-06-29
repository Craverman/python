import utils
from decimal import Decimal
from bs4 import BeautifulSoup
from requests import get

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
response = get(url)
date = response.headers['Date']
soup = BeautifulSoup(response.text, 'html.parser')
valute = soup.findAll('valute')
eur = valute[11].find('value').get_text()
eur = Decimal(eur.replace(',', '.'))
usd = valute[10].find('value').get_text()
usd = Decimal(usd.replace(',', '.'))
gbp = valute[2].find('value').get_text()
gbp = Decimal(gbp.replace(',', '.'))


print(utils.currency_rates(gbp))
print(date)





































