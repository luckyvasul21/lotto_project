import csv
import re
import sys
import time
from datetime import datetime, timedelta

import yaml

from selenium import webdriver
from selenium.common import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

# initiate browser
# with open(proj_path+'\\resources\\config.yml', "r") as f:
config = yaml.safe_load(open(sys.path[1] + '\\resources\\config.yml', "r"))

for lottery_select in ['EuroMillions', 'Lotto', 'Lotto54321', 'DailyMillion']:
    config_in_use = config[lottery_select]
    date_in_use = (datetime.now() + timedelta(days=-1)).strftime('%d %b %Y')

    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # options.add_argument('disable-gpu')
    options.add_argument('start-maximized')

    driver = webdriver.Chrome(service=Service(config['driver_path']), options=options)

    driver.get(config_in_use['url'])

    ignore_list = [ElementNotVisibleException, ElementNotSelectableException]
    wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=ignore_list)
    # wait = WebDriverWait(driver, timeout=10, poll_frequency=1)
    datePicker = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'rs-picker-toggle-placeholder')))

    ActionChains(driver).move_to_element(datePicker).click(datePicker).perform()

    selectDate = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[title^="'+date_in_use+'"]')))

    ActionChains(driver).move_to_element(selectDate).click(selectDate).perform()
    ActionChains(driver).move_to_element(selectDate).click(selectDate).perform()

    driver.find_element(By.CSS_SELECTOR, 'button.rs-picker-toolbar-right-btn-ok').click()

    time.sleep(2)

    for each_card in driver.find_elements(By.CSS_SELECTOR, config_in_use['results_card_selector']):
        src_attribute = each_card.find_element(By.TAG_NAME, 'img').get_attribute("src")

        lottery_type = re.findall(r'results/(.+).svg', src_attribute)[0]

        lottery_ball_row = each_card.find_elements(By.CSS_SELECTOR, config_in_use['lottery_ball_row_selector'])

        lottery_balls = [job.text for job in lottery_ball_row]

        filename = sys.path[1] + '\\prepared_assets\\'+lottery_type+'.csv'

        csvwriter = csv.writer(open(filename, 'a', newline=""))
        csvwriter.writerow(lottery_balls)
