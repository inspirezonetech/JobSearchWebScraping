from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pathlib import Path

import sys

def indeed_job_search(*args):
    
    browser = None

    PATH_TO_GECKO_DRIVER = './geckodriver'
    PATH_TO_CHROME_DRIVER = './chromedriver'

    if Path(PATH_TO_GECKO_DRIVER).is_file():
        options = webdriver.FirefoxOptions()
        if 'headless' in args:
            options.headless = True
        browser = webdriver.Firefox(executable_path=PATH_TO_GECKO_DRIVER, options=options)
    elif Path(PATH_TO_CHROME_DRIVER).is_file():
        options = webdriver.ChromeOptions()
        if 'headless' in args:
            options.headless = True
        browser = webdriver.Chrome(executable_path=PATH_TO_CHROME_DRIVER, options=options)
    else:
        print("Unable to find a webdriver.")
        return

    browser.get('https://www.indeed.com/worldwide')

    browser.implicitly_wait(5) 

    search_bar = browser.find_element_by_name('q')
    search_bar.send_keys('machine learning')
    search_bar = browser.find_element_by_name('l')
    search_bar.send_keys('New York')
    search_bar.send_keys(Keys.ENTER)

    browser.implicitly_wait(5) 

    search_results = browser.find_elements_by_xpath('//h2/a')
    search_descriptions=browser.find_elements_by_xpath('//div[@class="summary"]')
    
    descriptions=[]
    for element in search_descriptions:
        job_description=element.text
        descriptions.append(job_description)
        
    file = open("job_search.txt", 'a')
    file.write("\n")
    
    index=0
    for job_element in search_results:

        job_title = job_element.text
        job_link = job_element.get_attribute('href')
        

        file.write("%s | link: %s | description: %s \n" %(job_title, job_link, descriptions[index]))
        index=index+1


    browser.close()

if __name__ == "__main__":
    indeed_job_search(*sys.argv)