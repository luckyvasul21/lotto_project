import os
from behave import *

from src import handle_excel as handle_excel, common_methods as common_methods
from src.dates_handle import get_todays_weekday_name

use_step_matcher("re")

bookname = 'Sample.xlsx'

@when("user login into application")
def login_into_application(context):
    common_methods.login_into_lotto(context)

@when("user on results page")
def navigate_to_results_page(context):
# go to lotto results
    print(get_todays_weekday_name(), common_methods.get_todays_draw_name())

    context.browser.get('https://www.lottery.ie/dbg/results/view?game=' + common_methods.get_todays_draw_name() + '&draws=1')

@step("get today draw results")
def get_result_numbers(context):
    return common_methods.get_results(context)


@step("copy the results into lotto sheet")
def write_results_into_excel(context):
    lotto_data_this_week = get_result_numbers(context)
    # print(lotto_data_this_week)
# add draw date into array
    lotto_data_this_week.append(common_methods.get_draw_date(context))
    print(lotto_data_this_week)
    book = handle_excel.load_workbook(bookname)
    sheet = book[common_methods.get_todays_draw_name()]

    # print(handle_excel.get_max_row(sheet))
    get_last_row = handle_excel.get_max_row(sheet) + 1
    # print(get_last_row)

    for k in range(0, len(lotto_data_this_week)):
        # print(lotto_data_this_week[k])
        sheet.cell(row=get_last_row, column=k+1).value = lotto_data_this_week[k]
        # print(os.path.join(os.getcwd()+'\\resources\\', bookname))
        book.save(os.path.join(os.getcwd()+'\\resources\\', bookname))
        book.close()