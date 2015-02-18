#!/usr/bin/env python

'''
	Project Euler Problem 044 - Pentagon numbers
	----------------
	Description:

	Solution:
		
	----------------
	Haoliang Wang 02/06/2015
'''

from math import sqrt

def is_pentagon(n):
	x = (sqrt(24 * n + 1) + 1) / 6
	return int(x) == x

def is_hexagonal(n):
	x = (1 + sqrt(8 * n + 1)) / 4
	return int(x) == x

i = 286

while True:
	t = i * (i + 1) / 2
	if is_pentagon(t) and is_hexagonal(t):
		print t
		break
	i += 1