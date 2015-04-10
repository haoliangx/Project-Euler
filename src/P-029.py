#!/usr/bin/env python

'''
	Project Euler Problem 029 - Distinct powers
	----------------
	Description:
		How many distinct terms are in the sequence generated 
		by a ** b for 2 <= a <= 100 and 2 <= b <= 100?
	Solution:
		9183
	----------------
	Haoliang Wang 02/04/2015
'''

N = 100

s = set()

for a in range(2, N + 1):
	for b in range(2, N + 1):
		s.add(a ** b)

print len(s)