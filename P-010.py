#!/usr/bin/env python

'''
	Project Euler
	Problem 010 - Summation of primes
	Haoliang Wang
	01/28/2015
'''

'''
	Description:
		Find the sum of all the primes below two million.
	Solution:
		142913828922
'''

nsqrt = 2000000

l = [0] * nsqrt
i = 2
while i < nsqrt:
	j = 2
	while i * j < nsqrt:
		l[i * j] = 1
		j += 1
	i += 1
	while i < nsqrt and l[i] == 1:
		i += 1

print sum(filter(lambda x: l[x] == 0, range(2, nsqrt)))