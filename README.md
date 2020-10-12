# JobSearchWebScraping
Go to a job website, perform search and export job postings title and link to a file.

A full tutorial for this program is detailed on the [inspirezone.tech](https://inspirezone.tech) blog post: [Learn web scraping with python in minutes: The basics using selenium](https://inspirezone.tech/learn-web-scraping-with-python-in-minutes/)


## What this program does 

This is a web scraper written in python, using the selenium package. It will:
- Launch indeed.com/worldwide
- Perform a search for "machine learning"
- Export each job title and link to the job posting to a file


## How to use

### Browser and driver 
You need to have either Firefox or Chrome installed. You also need the corresponding driver for the browser.

For Firefox download geckodriver:
https://github.com/mozilla/geckodriver/releases

For Chrome download chromedriver:
https://chromedriver.chromium.org/downloads

### Setup Python and modules

Python and the following modules must be installed on the computer running this script.

Install Python and pip:
```
sudo apt-get install python
sudo apt-get install pip
```

Install selenium:
```
pip install selenium
```

### Run program
```
python job-search-web-scraping.py
```


