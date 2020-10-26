# JobSearchWebScraping
Go to a job postings website, perform search and export job title and description link to a file.

A full tutorial for this program is detailed on the [inspirezone.tech](https://inspirezone.tech) blog post: [Learn web scraping with python in minutes: The basics using selenium](https://inspirezone.tech/learn-web-scraping-with-python-in-minutes/). 

*See "blog-tutorial-original-code/job-search-web-scraping.py" for the original tutorial code.*

*You are welcome to contribute to this repo. See the **CONTRIBUTING.md** for more info*

## What this program does 

This is a web scraper written in python using the [selenium](https://www.selenium.dev/) package. It will:
- Launch indeed.com/worldwide
- Perform a search for "machine learning"
- Export each job posting title and link to a file


## How to use

### Download browser and driver 
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

You can run the program in headless mode adding the *headless* argument

```
python job-search-web-scraping.py headless
```

