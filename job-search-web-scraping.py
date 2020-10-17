from selenium import webdriver
from selenium.webdriver.common.keys import Keys


INDEED_URL = "https://www.indeed.com/worldwide"
PATH_TO_DRIVER = "./geckodriver"
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
        popup_cross = browser.find_element_by_class_name("popover-x-button-close")
        popup_cross.click()
    except:
        pass


def clean_up(browser, file):
    browser.close()
    file.close()


def indeed_job_search(search_term, pages=10, driver_path="./geckodriver"):
    browser = initial_search(search_term, driver_path)
    file = initialize_file(search_term)
    page_number = 1
    while True:
        search_results = get_jobs(browser)
        [write_job(job_element, file) for job_element in search_results]
        try:
            next_button = browser.find_element_by_xpath("//a[@aria-label='Next']")
            if page_number == pages:
                clean_up(browser, file)
            next_button.click()
            page_number += 1
            browser.implicitly_wait(WAIT_TIME)
            close_popup_if_present(browser)
        except Exception:
            clean_up(browser, file)
            exit


if __name__ == "__main__":
    indeed_job_search("machine learning", PAGES, PATH_TO_DRIVER)
