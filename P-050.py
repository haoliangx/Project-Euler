#!/usr/bin/env python

'''
	Project Euler Problem 050 - Pentagon numbers
	----------------
	Description:

	Solution:
		
	----------------
	Haoliang Wang 02/06/2015
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

primes = prime_list(10 ** 6)
ps = set(primes)

t = [0] * len(primes)
t[1] = primes
for k in range(2, len(primes)):
	print min(t[k-1])
	t[k] = []
	for i in range(len(primes) - k + 1):
		t[k].append(t[k - 1][i] + primes[i + k - 1])
	if min(t[k]) > 1000000:
		break

for i in range(k-1, 1, -1):
	flag = False
	for n in t[i]:
		if n in ps:
			print n
			flag = True
			break

	if flag:
		break
