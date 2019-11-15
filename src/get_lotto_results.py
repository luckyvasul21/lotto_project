from multiprocessing import context
from src.initiate_browser import *

proj_path = os.getcwd()[:os.getcwd().rfind('lottoproject')]+'lottoproject'
os.chdir(proj_path)

def lotto_go(context):
    open_browser(context)
    login(context)

# go to lotto results
    context.browser.get('https://www.lottery.ie/dbg/results/view?game=euromillions&draws=1')

# get results
    results_table = context.browser.find_elements_by_xpath('(//div[@class="winning-results"])')


    for i in range(len(results_table)-1):
        array=[]
        # print(i)
        numbers = context.browser.find_elements_by_xpath('(//div[@class="winning-results"])['+str(i+1)+']//label')
        assert len(numbers) == 7
        for j in range(len(numbers)):
            array.append(numbers[j].text)
            print(array[j])
        print(array)
        return array
# context.browser.quit()


if __name__ == '__main__':
    lotto_go(context)