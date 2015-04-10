#!/usr/bin/env python

'''
	Project Euler Problem 044 - Pentagon numbers
	----------------
	Description:

	Solution:
		5482660
	----------------
	Haoliang Wang 02/06/2015
'''

from math import sqrt

def is_pentagon(n):
	x = (sqrt(24 * n + 1) + 1.0) / 6.0
	return int(x) == x

i, found = 1, False

while not found:
	n = i * (3 * i - 1) / 2
	for j in reversed(xrange(1, i)):
		m = j * (3 * j - 1) / 2
		if is_pentagon(n - m) and is_pentagon(n + m):
			s = n - m
			found = True
			break
	i += 1

print s
