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

    # output tuples (word,1) in tab -delimited format
    stopwords = set(['the','and'])

    # output tuples (word, 1) in tab-delimited format
    for word in words:
       if word not in stopwords:
        print '%s\t%s' % (word, "1")

    # This loop is different
    # We want to exclude the stop words as we read through the line
    # We also want to add the comma 1 after the word for the reducer.py
