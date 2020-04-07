# Scraping tool
from bs4 import BeautifulSoup

# Internets navigation
from urllib.request import Request, urlopen

# Regex for cleaning the data we get from the internets
import re

# I love dataframes
import pandas as pd

# Making it so we don't request the data too fast from Metacritic (shh. we aren't a bot)
import time

# ??? This can probably be deleted. I don't think I'm using chain here
from itertools import chain

# Making it so our data scraping isn't as predictable (shh. we aren't a bot)
import random

# Creating index.
import uuid

nap = random.randint(30, 60)

# Scraping the main page to retrieve the number of pages we need to scrape in total
site = 'https://www.metacritic.com/browse/games/release-date/available/switch/date'
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site,headers=hdr)
page = urlopen(req)
soup = BeautifulSoup(page)

pages = soup.findAll('a', class_='page_num')
pages = re.findall('(\d+)(?!.*\d)',str(pages))
pages = int(pages[0])

sites = []
for i in range(pages):
    added_sites = site + '?page={}'.format(i)
    sites.append(added_sites)

## Scraping the URLs of all review pages for all games on Metacritic

URL = []
Title = []

def scrape_urls():

## Iterate through the page urls in order to scrape all the game titles and urls.

    for site in sites:

        nap = random.randint(30, 60)
        print("scraping " + site)
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = Request(site,headers=hdr)
        page = urlopen(req)
        soup = BeautifulSoup(page)

        BracketURLs = []
        urldivs = soup.findAll('div', class_='basic_stat')
        for url in urldivs:
            url = str(url.find('a'))
            url = url[9:]
            url = re.findall('.+?(?=">\n)', url)
            BracketURLs.append(url)

        BracketURLs = BracketURLs[0::2]
        BracketURLs = BracketURLs[:len(BracketURLs)-1]

        for sublist in BracketURLs:
            for item in sublist:
                URL.append(item)

        BracketTitle = []
        titledivs = soup.findAll('div', class_='basic_stat product_title')
        titledivs = titledivs[0:200]

        for title in titledivs:
            title = str(title.find('a'))
            title = re.findall('(?<=\\n)(.*?)(?=\\n)', title)
            title = [title.lstrip() for title in title]
            BracketTitle.append(title)

        for sublist in BracketTitle:
            for item in sublist:
                Title.append(item)

        print("sleeping for " + str(nap) + " seconds")
        time.sleep(nap)
        print("awake!")

    print('scraping complete!')

# Compile data into dataframe
    URLdf = pd.DataFrame([Title, URL]).transpose()
    URLdf.columns = ['Title', 'URL']

# Saving dataframe as CSV
    URLdf.to_csv('URLs.csv')
    print("Data saved to CSV as 'URLs.csv'")

scrape_urls()
