"""
For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

from iepy.webui.webui.settings import *

IEPY_VERSION = '0.9.6'
IEPY_LANG = 'en'
SECRET_KEY = '3ssx((2nkm$q_dpklxmt_6vn068*&v1zv#c&8jrx8(((6dbaqv'
DEBUG = True
TEMPLATE_DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/home/rafi/code/interview/factmata/assignment_iepy/assignment_iepy.sqlite',
    }
}

# For changing tokenization options, read here.
# http://nlp.stanford.edu/nlp/javadoc/javanlp/edu/stanford/nlp/process/PTBTokenizer.html
# You can use as key any of the "known options" listed on that page, and as value,
# use True or False (python names) for booleans, or strings when option requires a text
# CORENLP_TKN_OPTS = {
#     'latexQuotes': False
# }
