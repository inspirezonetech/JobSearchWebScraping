from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def indeed_job_search():
    
    PATH_TO_DRIVER = './geckodriver'

    browser = webdriver.Firefox(executable_path=PATH_TO_DRIVER)

    browser.get('https://www.indeed.com/worldwide')

    browser.implicitly_wait(5) 

    search_bar = browser.find_element_by_name('q')
    search_bar.send_keys('machine learning')
    search_bar.send_keys(Keys.ENTER)

    browser.implicitly_wait(5) 

    search_results = browser.find_elements_by_xpath('//h2/a')

    file = open("job_search.txt", 'a')
    file.write("\n")

    for job_element in search_results:

        job_title = job_element.text
        job_link = job_element.get_attribute('href')

        file.write("%s | link: %s \n" %(job_title, job_link))

    browser.close()

if __name__ == "__main__":
    indeed_job_search()