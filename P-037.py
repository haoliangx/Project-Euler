#!/usr/bin/env python

'''
	Project Euler Problem 037 - Truncatable primes
	----------------
	Description:
		Find the sum of the only eleven primes that are 
		both truncatable from left to right and right to left.
	Solution:
		748317
	----------------
	Haoliang Wang 02/06/2015
'''

# Guess the value to be lower than one million
M = 10 ** 6

s = []

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

ps = set(prime_list(M))

for n in ps - set([2, 3, 5, 7]):
	flag = True
	l = len(str(n))
	for i in range(1, l):
		if n / 10 ** (l - i) in ps and n % 10 ** i in ps:
			continue
		else:
			flag = False
			break
	if flag:
		s.append(n)

print sum(s)