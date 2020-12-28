import smtplib
import sys
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import basename
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from config import cfg


def send_email(sender_email_address, email_password,
               receiver_email_address, email_subject, email_smtp,
               email_body, file_path):
    """
    sender_email_address: sender email address
    email_password: sender email password
    receiver_email_address: receiver email password
    email_subject: email subject
    email_smtp: email smtp server
    email_body: email body
    file_path: file to attach in the email
    """
    # create an email message object
    message = MIMEMultipart()
    # configure email headers
    message['subject'] = email_subject
    message['From'] = sender_email_address
    message['To'] = receiver_email_address

    # attach the text file
    message.attach(MIMEText(email_body))
    part = MIMEApplication(open(file_path).read())
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % basename(file_path))
    message.attach(part)

    # set smtp server and port
    server = smtplib.SMTP(email_smtp, '587')
    # identify this client to the SMTP server
    server.ehlo()
    # secure the SMTP connection
    server.starttls()
    server.ehlo()
    # login to email account
    server.login(sender_email_address, email_password)
    # send email
    server.send_message(message)
    # close connection to server
    server.quit()


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

    browser.get('https://www.indeed.com')

    browser.implicitly_wait(5)

    search_bar = browser.find_element_by_name('q')
    search_bar.send_keys(cfg['keyword'])
    search_bar = browser.find_element_by_name('l')
    search_bar.send_keys(cfg['city'])
    search_bar.send_keys(Keys.ENTER)

    browser.implicitly_wait(5)

    search_results = browser.find_elements_by_xpath('//h2/a')

    file = open("job_search.txt", 'a')
    file.write("\n")

    for job_element in search_results:
        job_title = job_element.text
        job_link = job_element.get_attribute('href')

        file.write("%s | link: %s \n" % (job_title, job_link))
    send_email(cfg["sender_email"], cfg["sender_password"],
               cfg["receiver_email"],
               cfg["subject_email"],
               cfg["email_smtp"],
               cfg["body_email"],
               "job_search.txt")

    browser.close()


if __name__ == "__main__":
    indeed_job_search(*sys.argv)
