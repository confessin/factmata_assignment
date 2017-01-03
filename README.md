

Assignment:
===============

    Take the CSV and the statistics below (only 16)
    Build a script to get the training sentences and data to train on these somehow, and set this up.
    Find a way to label the sentences either supervised or semi-supervised
    Set up a development set and test set from this data. 
    Optimise a model on the dev set, and then run it on the test set you specify (this could be biased but for the interest of time, just be transparent and show me this model).


Headers of CSV:
===============

    Country Name
    Country Code
    Series Name
    Series Code
    2012
    2013
    2014
    2015
    2016


Statisitics:
===============

    Consumer price index (2010 = 100)	FP.CPI.TOTL
    Inflation, consumer prices (annual %)	FP.CPI.TOTL.ZG
    Pump price for diesel fuel (US$ per liter)	EP.PMP.DESL.CD
    Fertility rate, total (births per woman)	SP.DYN.TFRT.IN
    GDP growth (annual %)	NY.GDP.MKTP.KD.ZG
    GDP per capita (current US$)	NY.GDP.PCAP.CD
    GNI (current US$)	NY.GNP.MKTP.CD
    GDP (current US$)	NY.GDP.MKTP.CD
    GNI per capita, PPP (current international $)	NY.GNP.PCAP.PP.CD
    Health expenditure, total (% of GDP)	SH.XPD.TOTL.ZS
    Internet users (per 100 people)	IT.NET.USER.P2
    Life expectancy at birth, total (years)	SP.DYN.LE00.IN
    Population, total	SP.POP.TOTL
    Population growth (annual %)	SP.POP.GROW
    Renewable internal freshwater resources per capita (cubic meters)	ER.H2O.INTR.PC
    Prevalence of undernourishment (% of population)	SN.ITK.DEFC.ZS

Tasks

1. Get sentences by google search for each entity + country + (year)
2. Tag 
http://www.nltk.org/book/ch07.html



NOTES:
Example:
http://nbviewer.jupyter.org/github/skipgram/modern-nlp-in-python/blob/master/executable/Modern_NLP_in_Python.ipynb


Instead of sentences, can check whole paragraphs by Document Embedding with Paragraph Vectors?
https://arxiv.org/abs/1507.07998

Pipeline for QA?
http://iepy.readthedocs.io/en/latest/corpus_labeling.html#document-based-labeling


Findings:
    
    Most of the people when they talk about these statistics, they talk in increments and decrements.
