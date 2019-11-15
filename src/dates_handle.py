from datetime import date
import calendar



def get_todays_weekday_name():
    my_date = date.today()
    # print(calendar.day_name[my_date.weekday()])
    return calendar.day_name[my_date.weekday()]

def print_today():

    if get_todays_weekday_name() == 'Monday':
        print('1')
    elif get_todays_weekday_name() == 'Tuesday':
        print('2')
    elif get_todays_weekday_name() == 'Wednesday':
        print('3')
    elif get_todays_weekday_name() == 'Thursday':
        print('4')
    elif get_todays_weekday_name() == 'Friday':
        print('5')
    elif get_todays_weekday_name() == 'Saturday':
        print('6')
    elif get_todays_weekday_name() == 'Sunday':
        print('7')

if __name__ == '__main__':
    # get_todays_weekday_name()
    print_today()