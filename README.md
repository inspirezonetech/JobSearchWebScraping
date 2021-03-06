# JobSearchWebScraping

*You are welcome to contribute to this repo. See the [**CONTRIBUTING.md**](./CONTRIBUTING.md) for more info.*

![JobSearchWebScraping](https://inspirezone.tech/wp-content/uploads/2020/10/webscraping-python-selenium-1024x512.png)

## Tutorial available

A full tutorial walking you through this program is detailed on the [inspirezone.tech](https://inspirezone.tech) blog post: [Learn web scraping with python in minutes: The basics using selenium](https://inspirezone.tech/learn-web-scraping-with-python-in-minutes/).

The repo source files have gone through major modifications since the tutorial was written. You can see the original tutorial files under the folder [blog-tutorial-original-code/](blog-tutorial-original-code/). Use the code found in this folder to follow along with the blog tutorial.

## What this program does 

Go to a job postings website, perform search and export job title and description link to a file.

This is a web scraper written in python using the [selenium](https://www.selenium.dev/) package. It will:
- Launch indeed.com/worldwide
- Perform a search for "machine learning"
- Export each job posting title and link to a file

## How to use

### Step 1: Download browser and driver 

You need to have either Firefox or Chrome installed. You also need the corresponding driver for the browser.

For Firefox download geckodriver:
https://github.com/mozilla/geckodriver/releases

For Chrome download chromedriver:
https://chromedriver.chromium.org/downloads

### Step 2: Setup Python and modules

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

### Step 3: Run program

```
python job-search-web-scraping.py
```

You can run the program in headless mode adding the *headless* argument

```
python job-search-web-scraping.py headless
```

### For windows

Make sure that you download the correct browser driver version for your os, and for Windows make sure that it extensions is .exe 
