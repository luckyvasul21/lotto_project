import os
from selenium import webdriver

proj_path = os.getcwd()[:os.getcwd().rfind('lottoproject')]+'lottoproject'
os.chdir(proj_path)

def open_browser(context):

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

def login(context):
    context.browser.get('https://www.lottery.ie/account/login')

    context.browser.find_element_by_css_selector('input[name="username"]').click()
    context.browser.find_element_by_css_selector('input[name="username"]').clear()
    context.browser.find_element_by_css_selector('input[name="username"]').send_keys('xxx@xxx.com')

    context.browser.find_element_by_css_selector('input[name="password"]').click()
    context.browser.find_element_by_css_selector('input[name="password"]').clear()
    context.browser.find_element_by_css_selector('input[name="password"]').send_keys('*******')

    context.browser.find_element_by_css_selector('#loginSubmitButton').submit()
