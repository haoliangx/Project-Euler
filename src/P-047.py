#!/usr/bin/env python

'''
	Project Euler Problem 047 - Distinct prime factors
	----------------
	Description:

	Solution:
		
	----------------
	Haoliang Wang 02/06/2015
'''
from math import sqrt

m = 10 ** 6

# generate primes
t = [0] * m
i = 2
while i < m:
	j = 2
	while i * j < m:
		t[i * j] += 1
		j += 1
	i += 1
	while i < m and t[i] > 0:
		i += 1

for i in range(2, m - 4):
	if t[i] == t[i + 1] == t[i + 2] == t[i + 3] == 4:
		print i
		break