#!/usr/bin/env python

'''
	Project Euler Problem 001 - Multiples of 3 and 5
	----------------
	Description:
		Find the sum of all the multiples of 3 or 5 below 1000.
	Solution:
		233168
	----------------
	Haoliang Wang 01/27/2015
'''

MAX = 1000
print sum(filter(lambda x: not (x % 3 and x % 5), range(MAX)))
