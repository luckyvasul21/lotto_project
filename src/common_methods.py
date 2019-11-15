from src.dates_handle import get_todays_weekday_name
from src.initiate_browser import *


def login_into_lotto(context):
    open_browser(context)
    # login(context)


def get_todays_draw_name():
    # example: euromillions draw on tuesday, so taking results on Wednesday
    if get_todays_weekday_name() == 'Tuesday':
        return 'daily-million'
    elif get_todays_weekday_name() == 'Wednesday':
        return 'euromillions'
    elif get_todays_weekday_name() == 'Thursday':
        return 'lotto'
    elif get_todays_weekday_name() == 'Friday':
        return 'daily-million'
    elif get_todays_weekday_name() == 'Saturday':
        return 'euromillions'
    elif get_todays_weekday_name() == 'Sunday':
        return 'lotto'
    elif get_todays_weekday_name() == 'Monday':
        return 'daily-million'


def get_draw_date(context):
# get results date and day
    dateday = context.browser.find_element_by_css_selector('section > h4')
    # print(dateday.text)
    this_week_draw_day = dateday.text[0:3]
    this_week_draw_date = dateday.text[4:6]
    this_week_draw_month = dateday.text[7:11]
    this_week_draw_year = dateday.text[-4:]
    return dateday.text

def get_results(context):
 # get results
    results_table = context.browser.find_elements_by_xpath('(//div[@class="winning-results"])')

    # for i in range(len(results_table)-2): # 2 is given only to get first line, now lotto plus 1 and 2 and not taken yet WIP
    for i in range(1): # taking first result line WIP
        array=[]
        # print(i)
        numbers = context.browser.find_elements_by_xpath('(//div[@class="winning-results"])['+str(i+2)+']//label')


        # assert len(numbers) == 7
        for j in range(len(numbers)):
            array.append(numbers[j].text)
            # print(array[j])
        # print(array)
        return array
