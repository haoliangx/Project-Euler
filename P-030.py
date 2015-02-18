#!/usr/bin/env python

'''
	Project Euler Problem 030 - Digit fifth powers
	----------------
	Description:
		Find the sum of all the numbers that can be written 
		as the sum of fifth powers of their digits.
	Solution:
		443839
	----------------
	Haoliang Wang 02/04/2015
'''

print sum(k for k in xrange(10, 6 * 9 ** 5) if k == sum(int(c) ** 5 for c in str(k)))