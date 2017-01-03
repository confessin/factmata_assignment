#!/usr/bin/env python
# encoding: utf-8

"""
Contains functions for parsing raw text into entity tables.
"""

import spacy

__author__ = 'mrafi@mrafi.in (Mohammad Rafi)'

# This contains all the values validators based on a statistic
STATISTIC_VALIDATOR_MAP = {
        # Not less than 50 and not more than 200
        'FP.CPI.TOTL': lambda x: 50.0 < x < 200.0,
        }

STATISTIC_CONVERTER = {
        'FP.CPI.TOTL': lambda x: float(x),
        }


class Parser(object):

    """Docstring for Parser. """

    def __init__(self, statistic):
        """TODO: to be defined1. """
        self.nlp = spacy.load('en')
        self.statistic = statistic
        self.stat_validator = STATISTIC_VALIDATOR_MAP[self.statistic]
        self.convertor = STATISTIC_CONVERTER[self.statistic]

    def parse_by_statistic(self, value):
        try:
            value = self.convertor(value)
        except:
            return None
        if not self.stat_validator(value):
            return None
        return value

    def process_sentence(self, sent):
        countries = []
        possible_values = []
        doc = self.nlp(sent)
        for ent in doc.ents:
            if ent.label_ == 'GPE':
                countries.append(ent.text.lower())
            elif ent.label_ == 'CARDINAL':
                val = self.parse_by_statistic(ent.text.lower())
                if val:
                    possible_values.append()
