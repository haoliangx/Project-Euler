#!/usr/bin/env python

'''
	Project Euler Problem 040 - Champernowne's constant
	----------------
	Description:
		
	Solution:
		
	----------------
	Haoliang Wang 02/06/2015
'''
from operator import mul

s = ''.join([str(n) for n in xrange(1, 500000)])

print reduce(mul, [int(s[10 ** c - 1]) for c in range(0,7)])