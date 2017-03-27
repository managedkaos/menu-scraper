import datetime
import requests
from bs4 import BeautifulSoup
datetime.datetime.now().strftime('%A')

menus = {
        'ABC Riverside':'http://legacy.cafebonappetit.com/weekly-menu/145942', 
        'Grand Central': 'http://legacy.cafebonappetit.com/weekly-menu/146007', 
        'Circle 7': 'http://legacy.cafebonappetit.com/weekly-menu/146182', 
        'Buena Vista': 'http://legacy.cafebonappetit.com/weekly-menu/146581', 
        'Big D': 'http://legacy.cafebonappetit.com/weekly-menu/147508',
        'Kingswell': 'http://legacy.cafebonappetit.com/weekly-menu/151138'
    }

days = ['Monday','Tuesday','Wednesday','Thursday','Friday']

today = datetime.datetime.today().strftime('%A')
tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime('%A')

for cafe in menus:
    print cafe 
    r = requests.get(menus[cafe])
    data = r.text
    soup = BeautifulSoup(data, "lxml")

    for row in soup('div',{'class':'row'}):
        for spacer_day in row('div',{'class':'spacer day'}):
            for stationname in spacer_day('span',{'class':'stationname'}):
                if 'STOCKPOT' in stationname.contents[0]:
                    day_counter=0
                    for cell_menu_item in row('div',{'class':'cell_menu_item'}):
                        if today not in days[day_counter]:
                            day_counter += 1
                            continue

                        print "\t%s" % days[day_counter]

                        for menu_item in cell_menu_item('div',{'class':'menu-item'}):
                            for menu_item_description in menu_item('div',{'class':'menu-item-description'}):
                                for strong in menu_item_description('strong'):
                                    for span in strong('span'):
                                        print "\t\t%s" % span.contents[0]
                        break

