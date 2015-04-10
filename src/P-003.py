#!/usr/bin/env python

'''
	Project Euler Problem 003 - Largest prime factor
	----------------
	Description:
		What is the largest prime factor of the number 600851475143?
	Solution:
		6857
	----------------
	Haoliang Wang 01/27/2015
'''

from math import sqrt

N = 600851475143L
nsqrt = int(sqrt(N))

# Find Primes - Sieve of Eratosthenes
l = [0 for i in range(nsqrt)]
i = 2
while i < nsqrt:
	j = 2
	while i * j < nsqrt:
		l[i * j] = 1
		j += 1
	i += 1
	while i < nsqrt and l[i] == 1:
		i += 1

print max(filter(lambda x: l[x] == 0 and N % x == 0, xrange(2, nsqrt)))
