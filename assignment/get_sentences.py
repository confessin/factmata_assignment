#!/usr/bin/env python
# encoding: utf-8

"""
Scrape sentences.
"""

from config import TWITTER_KEYWORDS
from twitter import Twitter, OAuth
from TwitterSearch import *
import time
import csv


__author__ = 'mrafi@mrafi.in (Mohammad Rafi)'


token = "40271500-GrAwgP5SdBsuM8GawjP5MfvgQfZcKcBbduDHWD8If"
token_secret = "MiB8fslBtE7tsG9UVw9C34oPCOQsVd4BYkmXhU9QWk"
consumer_key = "WWJFhkGmollJljbbBl10qw"
consumer_secret = "eMEi72mgrAJ3k6uiZifZAVe3eF8Tt5BOj5JqiO3MA"


class SentenceGetter(object):

    """Docstring for SentenceGetter. """

    def __init__(self, country_list=None):
        """TODO: to be defined1. """
        self.country_list = country_list
        self.twitter = Twitter(
                auth=OAuth(token, token_secret, consumer_key, consumer_secret))
        # it's about time to create TwitterSearch object again
        self.ts = TwitterSearch(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token=token,
            access_token_secret=token_secret
        )

    def get_sentences(self, statistic, country="None"):
        # TODO: get it for every country.
        # twitter
        tso = TwitterSearchOrder()  # create a TwitterSearchOrder object
        tso.set_language('en')  # we want to see German tweets only
        #tso.set_include_entities(False)

        sentences = []
        for kwd in TWITTER_KEYWORDS.get(statistic):
            if country:
                kwd += " " + country
                print 'getting tweets for kwd: ', kwd
            tso.set_keywords(kwd.split())
            cnt = 1
            for tweet in self.ts.search_tweets_iterable(
                    tso, callback=self.my_callback_closure):
                sentences.append(tweet['text'])
                cnt += 1
                if cnt > 2000:  # 2k tweets per kwd.
                    break
        return sentences

    def my_callback_closure(self, current_ts_instance):  # accepts ONE argument: an instance of TwitterSearch
        queries, tweets_seen = current_ts_instance.get_statistics()
        if queries > 0 and (queries % 5) == 0:  # trigger delay every 5th query
            time.sleep(30)  # sleep for 60 seconds


if __name__ == "__main__":
    foo = SentenceGetter()
    sents = {}
    stats = ['FP.CPI.TOTL', 'FP.CPI.TOTL.ZG', 'EP.PMP.DESL.CD', 'SP.DYN.TFRT.IN']
    for i in stats:
        s = foo.get_sentences(i, 'USA')
        with open('data_usa_%s'%i, 'wb') as f:
            writer = csv.writer(f, delimiter=',',
                            quoting=csv.QUOTE_MINIMAL)
            for tweet in s:
                try:
                    writer.writerow([i, tweet])
                except:
                    continue
        sents[i] = s
        print 'done for ', i
    import ipdb
    ipdb.set_trace()
