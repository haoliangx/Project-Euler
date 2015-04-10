#!/usr/bin/env python

'''
	Project Euler
	Problem 012 - Highly divisible triangular number
	Haoliang Wang
	01/28/2015
'''

'''
	Description:
		What is the value of the first triangle number to have over five hundred divisors?
	Solution:
		76576500
'''

n = 500
m = 100000

# generate primes
t = [0] * m
i = 2
while i < m:
	j = 2
	while i * j < m:
		t[i * j] = 1
		j += 1
	i += 1
	while i < m and t[i] == 1:
		i += 1

# list of primes under m
primes = filter(lambda x: t[x] == 0, range(2, m))

from operator import mul

def factorize(n):
	while n > 1:
		for i in primes:
			if n % i == 0:
				n /= i
				yield i
				break

def num_divisors(n):
	f = list(factorize(n))
	return reduce(mul, [f.count(n) + 1 for n in set(f)], 1)

l = {}
i = 1
while True:
	t = i * (i + 1) / 2
	d1 = i / 2 if i % 2 == 0 else i
	d2 = (i + 1) if i % 2 == 0 else (i + 1) / 2
	if d1 not in l:
		l[d1] = num_divisors(d1)
	if d2 not in l:
		l[d2] = num_divisors(d2)
	l[t] = l[d1] * l[d2]
	if l[t] > n:
		print t
		break
	else:
		i += 1

