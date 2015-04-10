#!/usr/bin/env python

'''
	Project Euler Problem 022 - Names scores
	----------------
	Description:
		Find the sum of all products whose multiplicand/multiplier/product 
		identity can be written as a 1 through 9 pandigital.
	Solution:
		45228
	----------------
	Haoliang Wang 02/05/2015
'''

from itertools import permutations

s = []
for n in (''.join(n) for n in permutations('123456789*', 6) if '*' in n and n[0] != '*' and n[-1] != '*'):
	r = eval(n)
	if r < 9999 and len(set(n + str(r) + '0')) == 11: 
		s.append(r)

print sum(set(s))