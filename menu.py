import datetime
import argparse
from bonappetit_menus import cafes, days, get_weekly_menu

for cafe in cafes:
    print cafe 
    soup = get_weekly_menu(cafe)
    print "  soup"
    for row in soup('div',{'class':'row'}):
        for spacer_day in row('div',{'class':'spacer day'}):
            for stationname in spacer_day('span',{'class':'stationname'}):
                if 'STOCKPOT' in stationname.contents[0]:
                    day_counter=0
                    for cell_menu_item in row('div',{'class':'cell_menu_item'}):
                        print "\t%s" % days[day_counter]
                        for menu_item in cell_menu_item('div',{'class':'menu-item'}):
                            for menu_item_description in menu_item('div',{'class':'menu-item-description'}):
                                for strong in menu_item_description('strong'):
                                    for span in strong('span'):
                                        print "\t\t%s" % span.contents[0]
                        day_counter = (day_counter + 1) % 5

    print "  breakfast"
    for row in soup('div',{'class':'row'}):
        for spacer_day in row('div',{'class':'spacer day'}):
            for stationname in spacer_day('span',{'class':'stationname'}):
                if 'BREAKFAST' in stationname.contents[0]:
                    day_counter=0
                    for cell_menu_item in row('div',{'class':'cell_menu_item'}):
                        print "\t%s" % days[day_counter]
                        for menu_item in cell_menu_item('div',{'class':'menu-item'}):
                            for menu_item_description in menu_item('div',{'class':'menu-item-description'}):
                                for strong in menu_item_description('strong'):
                                    for span in strong('span'):
                                        print "\t\t%s" % span.contents[0]
                        day_counter = (day_counter + 1) % 5
