#!/usr/bin/env python

'''
	Project Euler Problem 046 - Pentagon numbers
	----------------
	Description:

	Solution:
		
	----------------
	Haoliang Wang 02/06/2015
'''

from math import sqrt

# Faster prime generation
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

i = 1
ps = set(prime_list(10 ** 5))

while True:
	n = i * 2 + 1
	found = False
	for j in reversed(xrange(int(sqrt(n / 2)) + 1)):
		if n - 2 * j * j in ps:
			found = True
	if not found:
		print n
		break
	i += 1