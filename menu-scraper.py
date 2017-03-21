import requests
from bs4 import BeautifulSoup

r = requests.get("http://legacy.cafebonappetit.com/weekly-menu/145942")

data = r.text

soup = BeautifulSoup(data, "lxml")

for thx in soup('div', {'class':'row'}):
    for thy in thx('div', {'class':'spacer day'}):
        for thz in thy('span', {'class':'stationname'}):
            print thz.contents[0]
            if ('STOCKPOT' in thz.contents[0]):
                print 'this is the corrct row!'
                print thx
