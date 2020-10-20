#!/usr/bin/env python3
import requests
import re
import time

from bs4 import BeautifulSoup


topic = 'data mining'


# returns title, author, year of publication and citations count for
# a given search on google scholar
def scrape_google_scholar_results(topic, filename=None):
    arg = topic.replace(' ', '+')
    url = 'https://scholar.google.com/scholar?q={}'.format(arg)
    response = requests.get(url)
    print(response)
    soup = BeautifulSoup(response.content, features='lxml')
    
    top10Data = []
    # list of tags for each search result
    results = soup.findAll('div', {'class': 'gs_ri'})
    print(results)
    for result in results:
        # title element
        titleText = result.select('h3')[0].get_text()
        title = titleText.split(']')[-1].strip()
        
        # element below title
        authorDateTag = result.find('div', {'class' : 'gs_a'})
        authorDateText = authorDateTag.get_text()
        authors = authorDateText.split('-')[0].strip()
        dateText = authorDateText.split('-')[-2]
        date = re.findall('\d\d\d\d', dateText)[-1]
        
        # cited by and related articles element
        citedByTag = result.find('div', {'class', 'gs_fl'})
        citedByText = citedByTag.get_text()
        citations = re.findall('Cited by \d+', citedByText)[0].split(' ')[2]
        
        top10Data.append('{}\t{}\t{}\t{}\n'.format(
                title, authors, date, citations))
        
    if filename is not None:
        with open(filename, 'w') as f:
            columnStr = 'Title\tAuthors\tYearOfPublication\tCitedBy\n'
            f.write(columnStr)
            for line in top10Data:
                f.write(line)
    
    return top10Data

scrape_google_scholar_results('data mining', 'data-mining.tsv')
time.sleep(3)
scrape_google_scholar_results('machine learning', 'machine-learning.tsv')
time.sleep(3)
scrape_google_scholar_results('artificial intelligence', 'artificial-intelligence.tsv')
time.sleep(3)
scrape_google_scholar_results('data analytics', 'data-analytics.tsv')
time.sleep(3)
scrape_google_scholar_results('text mining', 'text-mining.tsv')
time.sleep(3)
scrape_google_scholar_results('image processing', 'image-processing.tsv')