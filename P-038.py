#!/usr/bin/env python

'''
	Project Euler Problem 038 - Pandigital multiples
	----------------
	Description:
		What is the largest 1 to 9 pandigital 9-digit number that can 
		be formed as the concatenated product of an integer with 
		(1,2, ... , n) where n > 1?
	Solution:
		932718654
	----------------
	Haoliang Wang 02/06/2015
'''

m = 0

for n in range(2, 9):
	ul = 10 ** (9 / n + 1)
	ll = 10 ** (9 / n - 1) / n
	for k in range(ll, ul):
		t = ''.join([str(k * i) for i in range(1, n + 1)])
		s = set(t)
		s.discard('0')
		if len(s) == 9 == len(t) and m < int(t):
			m = int(t)

print m