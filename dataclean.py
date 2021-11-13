#!/usr/bin/env python
# coding: utf-8

# dataclean.py
# Data Cleaner
# Takes a text, returns that text, cleaned.

import os, pickle, re, string

def dataclean (text, fedReg=False):
    # Load the NLTK stopwords
    with  open(os.path.join(os.path.dirname(__file__), "stopwords.pkl"), "rb") as f:
        stopwords = pickle.load(f)
    
    # Convert to lower case
    text = text.lower()

    # Remove special characters, punctuations and replacing apostrophe
    text = re.sub('&[a-z]+;', '', text)
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans(string.punctuation,' '*len(string.punctuation)))
    text = text.replace("'", "")
         
    # Remove additional white spaces
    text = re.sub('[\W]{2,}', ' ', text)
    

    # Remove stopwords, including Federal Register stopwords
    # Let's add the following to dataclean's stopwords
    fedRegStopWords = {'rule', 'rules', 'final', 'federal', 'regulatory', 'filing', 'filings', 'regulation', 'regulations', 'volume', 'volumes', 'register', 'page', 'pages', 'number', 'online', 'government', 'publishing', 'office', 'gpo', 'www', 'gov', 'doc', 'no', 'department', 'cfr', 'part', 'parts', 'section', 'sections', 'title', 'titles', 'pursuant', 'paragraph', 'summary', 'background', 'supplementary', 'information', 'national', 'nation', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'}
    if fedReg == True:
        stopwords = stopwords.union(fedRegStopWords)
    text = " ".join([word for word in text.split(" ") if word not in stopwords])
    
    return text

# test
# print(dataclean("How now brown cow?"))