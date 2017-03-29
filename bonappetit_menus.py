import requests
from bs4 import BeautifulSoup

# URLs for each cafe's main menu
menus = {
        'ABC Riverside':'http://wds.cafebonappetit.com/cafe/abc-riverside/',
        'Grand Central': 'http://wds.cafebonappetit.com/cafe/grand-central-cafe/',
        'Circle 7': 'http://wds.cafebonappetit.com/cafe/circle-7-cafe/',
        'Buena Vista': 'http://wds.cafebonappetit.com/cafe/buena-vista-cafe/', 
        'Big D': 'http://wds.cafebonappetit.com/cafe/big-d-cafe/',
        'Kingswell': 'http://wds.cafebonappetit.com/cafe/the-prospect-cafe/'
    }

# weekdays
days = ['Monday','Tuesday','Wednesday','Thursday','Friday']

# a function to return the content of the current weekly menu for a given cafe
def get_weekly_menu(cafe):

    # make a request to the main menu URL for the specified cafe
    r = requests.get(menus[cafe])

    # convert the response text to soup
    soup = BeautifulSoup(r.text, "lxml")

    # find the link for the current weekly menu
    link = soup.findAll('a', href=True, text='View/Print Weekly Menu')
    weekly_menu_link = link[0]['href']

    # make a request to the currently weekly menu URL
    r = requests.get(weekly_menu_link)

    # return the soup object
    return BeautifulSoup(r.text, "lxml")
