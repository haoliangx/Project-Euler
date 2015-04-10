#!/usr/bin/env python

'''
	Project Euler Problem 019 - Counting Sundays
	----------------
	Description:
		How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
	Solution:
		171
	----------------
	Haoliang Wang 01/29/2015
'''

from datetime import datetime
from itertools import product

def is_sunday((y, m)):
	return datetime(y, m, 1).weekday() == 6

print len(filter(is_sunday, product(range(1901, 2001), range(1, 13))))