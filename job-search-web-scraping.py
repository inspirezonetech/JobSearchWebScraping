import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

INDEED_URL = "https://www.indeed.com/worldwide"
PATH_TO_DRIVER = "./geckodriver/geckodriver.exe"
WAIT_TIME = 5
PAGES = 10


def initial_search(search_term, driver_path):
    browser = webdriver.Firefox(executable_path=driver_path)

    browser.get(INDEED_URL)

    browser.implicitly_wait(WAIT_TIME)

    search_bar = browser.find_element_by_name("q")
    search_bar.send_keys(search_term)
    search_bar.send_keys(Keys.ENTER)

    browser.implicitly_wait(WAIT_TIME)
    return browser


def initialize_file(search_term):
    file = open(f"job_search_{search_term.replace(' ','_')}.txt", "a")
    file.write("\n")
    return file


def write_job(job_element, file):
    job_title = job_element.text
    job_link = job_element.get_attribute("href")

    file.write("%s | link: %s \n" % (job_title, job_link))


def get_jobs(browser):
    return browser.find_elements_by_xpath("//h2/a")


def close_popup_if_present(browser):
    try:

        popup_cross = browser.find_elements_by_xpath(
            "//button[contains(@class,'popover-x-button-close')]"
        )
        popup_cross[0].click()
        return True
    except:
        return False


def clean_up(browser, file):
    try:
        browser.close()
    except:
        pass
    file.close()


def indeed_job_search(search_term, pages=10, driver_path="./geckodriver"):
    popup_encountered = False
    browser = initial_search(search_term, driver_path)
    file = initialize_file(search_term)
    page_number = 1
    while True:
        if not popup_encountered:
            time.sleep(WAIT_TIME)
            popup_encountered = close_popup_if_present(browser)
        search_results = get_jobs(browser)
        [write_job(job_element, file) for job_element in search_results]
        try:
            browser.implicitly_wait(WAIT_TIME)
            next_button = browser.find_element_by_xpath("//a[@aria-label='Next']")
            if page_number == pages:
                clean_up(browser, file)
            next_button.click()
            page_number += 1
        except Exception:
            clean_up(browser, file)
            exit


if __name__ == "__main__":
    indeed_job_search("machine learning", PAGES, PATH_TO_DRIVER)
