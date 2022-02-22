#!/usr/bin/env python
# coding: utf-8

# dataclean.py
# Data Cleaner
# Takes a text, returns that text, cleaned.

import os, pickle, re, string

def dataclean (text, additional_stopwords={}]):
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
    

    # Remove stopwords, including any additional user-supplied stopwords
    # Let's add the following to dataclean's stopwords
    stopwords = stopwords.union(additional_stopwords)
    text = " ".join([word for word in text.split(" ") if word not in stopwords])
    
    return text

