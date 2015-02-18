#!/usr/bin/env python

'''
	Project Euler Problem 024 - Lexicographic permutations
	----------------
	Description:
		What is the millionth lexicographic permutation of 
		the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
	Solution:
		2783915460
	----------------
	Haoliang Wang 02/03/2015
'''
from math import floor, factorial as f

N = 1000000
n = 10

s = []
t = range(n)

for i in range(1, n + 1):
	d = int(floor(N / f(n - i)))
	s.append(t.pop(d))
	N -= f(n - i) * d
	if N == 0:
		s += list(reversed(t))
		break

print s

