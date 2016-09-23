#!/usr/bin/env python

"""
A filter that convert upper case to lower case.
"""

import fileinput


def process(line):
    """For each line of input, lower."""
    print(line[:-1].lower())


for line in fileinput.input():
    process(line)

