def bethanys_code():
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
    INCORRECT WORD FREQ DICT SO THIS IS INCORRECT AS WELL
    ok -- for the given text (already in the file), you should get {2: 0.96296296296296302, 1: 0.88888888888888884, 3: 0.0} as the output
    '''
    
    
    
    
def kshitijs_code():
    '''
    Created on Mon Aug 21 18:26:24 2017

    @author: bethanygarcia

    Create a function more_frequent(distribution) that takes a word frequency
    dictionary (like that made in word_cound_distribution) and outputs a dictionary
    with the same keys as those in distribution (the number of times a group of
    words appears in the text), and values corresponding to the fraction of words
    that occur with more frequency than that key.
    Call more_frequent(distribution), and store as cumulative.

    Example-

    text = This is my test text.  We're keeping this text short to keep things manageable.
    The quick brown fox jumps over the lazy lazy lazy dog. Yes, the dog was very lazy.

    Word frequencies are:
    {'this': 2, 'is': 1, 'my': 1, 'test': 1, 'text': 2, 'were': 1, 'keeping': 1, 'short': 1, 'to': 1, 'keep': 1, 'things': 1, 'manageable': 1,
    'the': 3, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 4, 'dog': 2, 'yes': 1, 'was': 1, 'very': 1}

    Frequency of frequencies
    {1: 18, 2: 3, 3: 1, 4: 1}

     Result to be cal:
     {1: 0/18+3+1+1, 2: 18/18+3+1+1, 3: 18+3/18+3+1+1, 4: 18+3/18+3+1+1}

    '''
    '''
    Solution in py2 by @stain88 in #fluent-python in codebuddies.org slack
    def more_frequent(distribution):

        return dict(map(lambda (k,v): (k, sum(x for x in sorted(distribution.values()) if x > v) / float(sum(distribution.values()))), distribution.iteritems()))
    '''
    
    text = '''This is my test text.  We're keeping this text short to keep things manageable.
    The quick brown fox jumps over the lazy lazy lazy dog. Yes, the dog was very lazy.'''
    
    import string
    import operator
    from collections import OrderedDict as odict
    
    text = text.lower()
    only_letters = [char_ for char_ in text if char_ in string.ascii_letters or char_ == ' ']
    words_list = ''.join(only_letters).split()
    word_freq = {word: words_list.count(word) for word in words_list}
    print('Word frequencies are:')
    print(word_freq)
    print()
    
    score_freq = {v: list(word_freq.values()).count(v) for k, v in word_freq.items()}
    score_freq = odict(sorted(score_freq.items(), key=operator.itemgetter(1)))
    print('Frequency of frequencies are:')
    print(score_freq)
    print()
    
    freq_greater = {k: [in_v for in_v in score_freq.values() if in_v > v] for k, v in
                    score_freq.items()}
    print('Slecting greater than current val frequencies:')
    print(freq_greater)
    print()
    
    freq_total = sum(score_freq.values())
    freq_distrib_distrib = {k: sum(v) / freq_total for k, v in freq_greater.items()}
    print('frequency distribution of frequency distribution:')
    print(freq_distrib_distrib)
    print()
    
def kshitijs_code_compact():
    '''
    Created on Mon Aug 21 18:26:24 2017

    @author: bethanygarcia

    Create a function more_frequent(distribution) that takes a word frequency
    dictionary (like that made in word_cound_distribution) and outputs a dictionary
    with the same keys as those in distribution (the number of times a group of
    words appears in the text), and values corresponding to the fraction of words
    that occur with more frequency than that key.
    Call more_frequent(distribution), and store as cumulative.

    Example-

    text = This is my test text.  We're keeping this text short to keep things manageable.
    The quick brown fox jumps over the lazy lazy lazy dog. Yes, the dog was very lazy.

    Word frequencies are:
    {'this': 2, 'is': 1, 'my': 1, 'test': 1, 'text': 2, 'were': 1, 'keeping': 1, 'short': 1, 'to': 1, 'keep': 1, 'things': 1, 'manageable': 1,
    'the': 3, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 4, 'dog': 2, 'yes': 1, 'was': 1, 'very': 1}

    Frequency of frequencies
    {1: 18, 2: 3, 3: 1, 4: 1}

     Result to be cal:
     {1: 0/18+3+1+1, 2: 18/18+3+1+1, 3: 18+3/18+3+1+1, 4: 18+3/18+3+1+1}

    '''
    '''
    Solution in py2 by @stain88 in #fluent-python in codebuddies.org slack
    def more_frequent(distribution):

        return dict(map(lambda (k,v): (k, sum(x for x in sorted(distribution.values()) if x > v) / float(sum(distribution.values()))), distribution.iteritems()))
    '''
    
    text = '''This is my test text.  We're keeping this text short to keep things manageable.
    The quick brown fox jumps over the lazy lazy lazy dog. Yes, the dog was very lazy.'''
    
    import string
    import operator
    from collections import OrderedDict as odict
    
    
    # Create word frequency dict.
    text = text.lower()
    only_letters = [char_ for char_ in text if char_ in string.ascii_letters or char_ == ' ']
    words_list = ''.join(only_letters).split()
    word_freq = {word: words_list.count(word) for word in words_list}
    
    # create dict of frequecy of word frequencies
    score_freq = {v: list(word_freq.values()).count(v) for k, v in word_freq.items()}
    score_freq = odict(sorted(score_freq.items(), key=operator.itemgetter(1)))
    
    # Create dict where values are list of frequencies greater than frequency of current key
    freq_greater = {k: [in_v for in_v in score_freq.values() if in_v > v] for k, v in
                    score_freq.items()}
   # sum the list of greater frequency(cumsum final value) and divide by total frequency.
    freq_total = sum(score_freq.values())
    freq_distrib_distrib = {k: sum(v) / freq_total for k, v in freq_greater.items()}
    
    return freq_distrib_distrib
    
print(kshitijs_code_compact())

"""
Bethany's answer:{1: 0.95652173913043481, 2: 0.91304347826086962, 3: 0.78260869565217395, 4: 0.0}
My answer:{1: 0.0, 2: 0.782608695652174, 3: 0.9130434782608695, 4: 0.9130434782608695}

Bethany's solution says "95% of the words do not have a frequency of 4, 91% do not have a
frequency of 3 or 4, 78% do not have a frequency of 2,3 or 4, and 0% do not have a frequency less than 1"

our solution is saying "no words have a frequency less than 1, 78% occur once, 91% occur once or twice, 91% occur less than 4 times"

"""
    
    
