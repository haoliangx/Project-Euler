#!/usr/bin/env python

'''
	Project Euler Problem 049 - Prime permutations
	----------------
	Description:
		What 12-digit number do you form by 
		concatenating the three terms in this sequence?
	Solution:
		
	----------------
	Haoliang Wang 02/12/2015
'''

def prime_list(num):
	if num < 2:
		return []
	p = range(1, num, 2)
	p[0] = 2
	ub = int(num ** (1 / 2.0))
	for k in range(3, ub + 1, 2):
		if p[(k + 1) / 2 - 1]:
			p[((k * k + 1) / 2) - 1: num / 2 + 1: k] = [0] * len(p[((k * k + 1) / 2) - 1: num / 2 + 1: k])
	return filter(lambda x: x > 0, p)

primes = set(prime_list(10000))
s = {}

for p in sorted(primes):
	if p > 1000:
		t = int(''.join(sorted(str(p))))
		if t > 1000:
			if t in s:
				s[t].append(p)
			elif t in primes:
				s[t] = [t, ]
			else:
				s[t] = []

for i in s:
	if len(s[i]) == 3:
		s[i].sort()
		if s[i][1] - s[i][0] == s[i][2] - s[i][1]:
			print s[i]