import os
from multiprocessing import context

import time
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

proj_path = os.getcwd()[:os.getcwd().rfind('lottoproject')]+'lottoproject'
os.chdir(proj_path)

def lotto_go(context):

# initiate browser
    chrome_path = proj_path+'/resources/chromedriver.exe'
    # print(chrome_path)
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # options.add_argument('disable-gpu')
    options.add_argument('start-maximized')
    prefs = {"profile.default_content_settings.popups": 0,
             "download.default_directory": r""+proj_path+"/result/", # IMPORTANT - ENDING SLASH V IMPORTANT
             "directory_upgrade": True}
    options.add_experimental_option("prefs", prefs)

    context.browser = webdriver.Chrome(chrome_path, chrome_options=options)
    context.browser.implicitly_wait(30)

# login
    context.browser.get('https://www.lottery.ie/account/login')

    context.browser.find_element_by_css_selector('input[name="username"]').click()
    context.browser.find_element_by_css_selector('input[name="username"]').clear()
    context.browser.find_element_by_css_selector('input[name="username"]').send_keys('luckyvasul@gmail.com')

    context.browser.find_element_by_css_selector('input[name="password"]').click()
    context.browser.find_element_by_css_selector('input[name="password"]').clear()
    context.browser.find_element_by_css_selector('input[name="password"]').send_keys('Greeg8989')

    context.browser.find_element_by_css_selector('#loginSubmitButton').submit()

# go to lotto play online
    context.browser.get('https://www.lottery.ie/games/lotto')

# lotto quick pick 2 lines
    context.browser.find_element_by_css_selector('#playSlip0line1 > ul > li[class="info-qp"]').click()
    time.sleep(1)
    context.browser.find_element_by_css_selector('#playSlip0line2 > ul > li[class="info-qp"]').click()
    time.sleep(1)



# check Add lotto plus is also selected
    # be default is selected, so check the ticket price value, should be 5 euros for 2 lines selected
    totalAmount = context.browser.find_element_by_css_selector('#totalAmount')
    assert totalAmount.text == '€5.00'

    playNow_button = context.browser.find_element_by_css_selector('#playNow').click()

# check totalAmount displayed for selected lines == Amount to pay
    totalPrice = context.browser.find_element_by_css_selector('#totalAmount')
    assert totalAmount.text == totalPrice.text

# check enough balance in accunt before buying ticket
    wallet = context.browser.find_element_by_css_selector('li.info-balance span.wallet')
    print(wallet.text)
# buy ticket
#     context.browser.find_element_by_css_selector('button[data-test-id="buy_ticket_button"]').click()



    # context.browser.quit()

if __name__ == '__main__':
    lotto_go(context)