#!/usr/bin/env python

'''
	Project Euler Problem 021 - Amicable numbers
	----------------
	Description:
		Evaluate the sum of all the amicable numbers under 10000.
	Solution:
		31626
	----------------
	Haoliang Wang 01/30/2015
'''

l = {}
def d(n):
	if n not in l:
		l[n] = sum([m + n / m for m in range(1, int(n ** 0.5)) if n % m == 0]) - n
	return l[n]

print sum(filter(lambda x: x == d(d(x)) and x != d(x), range(4, 10000)))
