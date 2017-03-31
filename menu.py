import datetime
import argparse
from bonappetit_menus import menus, days, get_weekly_menu

parser = argparse.ArgumentParser()

parser.add_argument(
    '-c', 
    '--cafe', 
    required=False, 
    type=str,
    choices=['abc7','abcriverside'],
    help="the cafe(s) menu that will be looked up")

args = parser.parse_args()

today = datetime.datetime.today().strftime('%A')
tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime('%A')

for cafe in menus:
    print cafe 
    soup = get_weekly_menu(cafe)

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

