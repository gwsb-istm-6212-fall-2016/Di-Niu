#!/usr/bin/env python

"""
A filter that split.
"""

import fileinput
import re

def process(line):
    """For each line of input, remove the stop words."""
    
    line = re.findall(r'\w+',line)
    stopwords = ['the', 'of', 'to', 'and', 'a', 'in', 'is', 'it', 'you', 'that']
    
    for word in line:
        if word not in stopwords:
            print(word.strip())
            
for line in fileinput.input():
    process(line)
