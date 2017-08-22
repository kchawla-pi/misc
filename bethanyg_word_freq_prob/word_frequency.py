#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 18:26:24 2017

@author: bethanygarcia

Create a function more_frequent(distribution) that takes a word frequency 
dictionary (like that made in word_cound_distribution) and outputs a dictionary
with the same keys as those in distribution (the number of times a group of 
words appears in the text), and values corresponding to the fraction of words 
that occur with more frequency than that key.
Call more_frequent(distribution), and store as cumulative.
"""

import os
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from itertools import accumulate 

book_dir = "./Books"

text = "This is my test text.  We're keeping this text short to keep things manageable.\
The quick brown fox jumps over the lazy lazy lazy dog. Yes, the dog was very lazy."

def count_words(text):
    """Count the number of thimes each word occurs in text (str).
    Return dictionary where keys are unique words and values are 
    word counts."""
    
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"']
    for char in skips:
        text.replace(char, "")

        
    word_counts = {}
    for word in text.split(" "):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    return word_counts
    
def count_words_fast(text):
    """Count the number of thimes each word occurs in text (str).
    Return dictionary where keys are unique words and values are 
    word counts. Uses Counter from collections"""
    
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"']
    for char in skips:
        text.replace(char, "")
        
    word_counts = Counter(text.split(" "))
    
    return word_counts


def read_book(title_path):
    """Read a book and return it as a string."""
    
    with open(title_path, "r",encoding='utf8') as current_file:
        text = current_file.read()
        text.replace("\n", "").replace("\r", "")
    
    return text

def word_stats(word_counts):
    """Returns number of unique words and word frequencies"""
    num_unique = len(word_counts)
    counts = word_counts.values()
    
    return (num_unique, counts)


def word_count_distribution(book_string):
    count_distribution = Counter(count_words_fast(book_string).values())
    
    return count_distribution
    
distribution = word_count_distribution(text)


def more_frequent(distribution):
    cnt = list(distribution.keys())
    more_freq = 1 - np.cumsum(list(sorted(distribution.values()))) / np.cumsum(list(sorted(distribution.values())))[-1]
    freq_dict =  {k:v for k, v in zip(cnt, more_freq)}
    
    return freq_dict


'''
ok -- for the given text (already in the file), you should get {2: 0.96296296296296302, 1: 0.88888888888888884, 3: 0.0} as the output
'''
