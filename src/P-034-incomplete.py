#!/usr/bin/env python

'''
	Project Euler Problem 034 - Digit factorials
	----------------
	Description:
		Find the sum of all numbers which are equal
		to the sum of the factorial of their digits.
	Solution:
		40730
	----------------
	Haoliang Wang 01/30/2015
'''

from math import factorial

f = [factorial(k) for k in range(10)]

def lp(depth, mx, al):
	if depth == 1:
		al = [[x] for x in range(mx + 1)]
	else:
		al = [[i] + pre for i in range(mx + 1) for pre in lp(depth - 1, mx - i, al)]                
	return al

def check(t):
	return sum(f[int(c)] for c in str(t)) == t

# one-liner
print sum(set(filter(lambda t: t > 10 and check(t), (sum([f[x + 1] * y for x, y in enumerate(s)]) for s in lp(9, 7, [])))))

# Expanded
r = set()
for s in lp(9, 7, []):
	t = sum([f[x + 1] * y for x, y in enumerate(s)])
	if t > 10 and sum(f[int(c)] for c in str(t)) == t:
		r.add(t)

print sum(r)