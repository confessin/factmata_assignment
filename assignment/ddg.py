#!/usr/bin/env python
# encoding: utf-8

"""
Duck Duck go search
"""

from config import TWITTER_KEYWORDS
import csv
import requests
from lxml import html
import time

def search(keywords, max_results=None):
    url = 'https://duckduckgo.com/html/'
    params = {
        'q': keywords,
        's': '0',
    }

    yielded = 0
    while True:
        res = requests.post(url, data=params)
        doc = html.fromstring(res.text)
        results = [a.text_content() for a in doc.cssselect('.result__snippet')]
        for result in results:
            yield result
            time.sleep(0.1)
            yielded += 1
            if max_results and yielded >= max_results:
                return

        try:
            form = doc.cssselect('.results_links_more form')[-1]
        except IndexError:
            return
        params = dict(form.fields)


import json
import scrapy
 
 
class SpidyQuotesSpider(scrapy.Spider):
    name = 'spidyquotes'
    quotes_base_url = 'http://spidyquotes.herokuapp.com/api/quotes?page=%s'
    start_urls = [quotes_base_url % 1]
    download_delay = 1.5
 
    def parse(self, response):
        data = json.loads(response.body)
        for item in data.get('quotes', []):
            yield {
                'text': item.get('text'),
                'author': item.get('author', {}).get('name'),
                'tags': item.get('tags'),
            }
        if data['has_next']:
            next_page = data['page'] + 1
            yield scrapy.Request(self.quotes_base_url % next_page)


if __name__ == "__main__":
    #foo = SpidyQuotesSpider()
    #foo.parse()
    stats = ['FP.CPI.TOTL', 'FP.CPI.TOTL.ZG', 'EP.PMP.DESL.CD', 'SP.DYN.TFRT.IN']
    for i in stats:
        for kwd in TWITTER_KEYWORDS.get(i):
            q = 'site:reddit.com ' + kwd + ' america'
            with open('data_usa_reddit_%s.csv' % i, 'wb') as f:
                writer = csv.writer(f, delimiter=',',
                                quoting=csv.QUOTE_MINIMAL)
                for subtext in search(q, max_results=10):
                    try:
                        writer.writerow([i, subtext])
                    except:
                        continue
            print 'done for ', i, q
