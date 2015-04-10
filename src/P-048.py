#!/usr/bin/env python

'''
	Project Euler Problem 048 - Self powers
	----------------
	Description:
		Find the last ten digits of the series, 
		1^1 + 2^2 + 3^3 + ... + 1000^1000.
	Solution:
		9110846700
	----------------
	Haoliang Wang 02/06/2015
'''

mod = 10 ** 10

print reduce(lambda x, y: (x + pow(y, y, mod)) % mod, xrange(1, 1001))