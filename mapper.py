#!/usr/bin/env python
import sys

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # make lower case
    line = line.lower()

    # split the line into words; splits on any whitespace
    words = line.split()

    #remove punctuation
    #punct  = set(['.',',',';',':','!','?'])
    #no_punct = '' 
    #for char in words:
	#if char not in punct:
	    # words = words + no_punct 

    # output tuples (word, 1) in tab-delimited format - removing stopwords (stops)
    from sklearn.feature_extraction import stop_words 
    stops = set(stop_words.ENGLISH_STOP_WORDS)
 
    for word in words:
     if word not in stops:
        print '%s\t%s' % (word, "1")
