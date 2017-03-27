import requests
from bs4 import BeautifulSoup

menus = {
        'ABC Riverside':'http://wds.cafebonappetit.com/cafe/abc-riverside/',
        'Grand Central': 'http://wds.cafebonappetit.com/cafe/grand-central-cafe/',
        'Circle 7': 'http://wds.cafebonappetit.com/cafe/circle-7-cafe/',
        'Buena Vista': 'http://wds.cafebonappetit.com/cafe/buena-vista-cafe/', 
        'Big D': 'http://wds.cafebonappetit.com/cafe/big-d-cafe/',
        'Kingswell': 'http://wds.cafebonappetit.com/cafe/the-prospect-cafe/'
    }

days = ['Monday','Tuesday','Wednesday','Thursday','Friday']

def get_weekly_menu(cafe):
    r = requests.get(menus[cafe])
    data = r.text
    soup = BeautifulSoup(data, "lxml")
    print soup
