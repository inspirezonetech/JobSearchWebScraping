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
    indeed_job_search()