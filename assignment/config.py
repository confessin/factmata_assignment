#!/usr/bin/env python
# encoding: utf-8

"""
Creates configs
"""
import csv


__author__ = 'mrafi@mrafi.in (Mohammad Rafi)'

CSV_FILE_NAME = '/home/rafi/code/interview/factmata/EMNLP_worldbank_2012-2016.csv'

#######################################################################
#                             Extra Info.                             #
#######################################################################
ALLOWED_FEATURES = [
        "FP.CPI.TOTL",
        "FP.CPI.TOTL.ZG",
        "EP.PMP.DESL.CD",
        "SP.DYN.TFRT.IN",
        ]

TWITTER_KEYWORDS = {
        "FP.CPI.TOTL": ["consumer price", "consumer price index"],
        "FP.CPI.TOTL.ZG": ["inflation", "inflation rate"],
        "EP.PMP.DESL.CD": ["diesel prices OR cost"],
        "SP.DYN.TFRT.IN": ["fertility rate", "birth rate"],
        #"NY.GDP.MKTP.KD.ZG": [],
        #"NY.GDP.PCAP.CD": [],
        #"NY.GNP.MKTP.CD": [],
        #"NY.GDP.MKTP.CD": [],
        #"NY.GNP.PCAP.PP.CD": [],
        #"SH.XPD.TOTL.ZS": [],
        #"IT.NET.USER.P2": [],
        #"SP.DYN.LE00.IN": [],
        #"SP.POP.TOTL": [],
        #"SP.POP.GROW": [],
        #"ER.H2O.INTR.PC": [],
        #"SN.ITK.DEFC.ZS": [],
        }


class DataWorldBank(object):

    """Docstring for DataWorldBank. """

    def __init__(self):
        """TODO: to be defined1. """
        self.file_name = CSV_FILE_NAME
        self.HEADER = [
                "country_name",
                "country_code",
                "series_name",
                "series_code",
                "2012",
                "2013",
                "2014",
                "2015",
                "2016"
                ]
        self.country_list = set()

    def read(self):
        self.data = []
        with open(CSV_FILE_NAME, 'rU') as f:
            reader = csv.reader(f, delimiter=',')
            reader.next()
            for row in reader:
                row = self.clean_row(row)
                n_row = dict(zip(self.HEADER, row))
                if n_row['series_code'] in ALLOWED_FEATURES:
                    n_row['twitter_keywords'] = TWITTER_KEYWORDS.get(n_row['series_code'])
                    self.data.append(n_row)
                    self.country_list.add(n_row['country_name'].lower())

    def clean_row(self, row):
        n_row = []
        for el in row:
            if el and el not in ('..', '', '...'):
                n_row.append(el)
            else:
                n_row.append(None)
        return n_row


if __name__ == "__main__":
    foo = DataWorldBank()
    foo.read()
