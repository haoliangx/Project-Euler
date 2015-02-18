#!/usr/bin/env python

'''
	Project Euler Problem 035 - Circular primes
	----------------
	Description:
		How many circular primes are there below one million?
	Solution:
		55
	----------------
	Haoliang Wang 02/05/2015
'''

N = 10 ** 6

# Not used. interesting array slice
def lshift_k(n, k):
	return int(str(n)[k::] + str(n)[:k:])

def rshift(n):
	nl = 10 ** (len(str(n)) - 1)
	t = n / 10 + (n % 10) * nl
	while t != n:
		yield t
		t = t / 10 + (t % 10) * nl

l = [0 for i in range(N)]
i = 2
while i < N:
	j = 2
	while i * j < N:
		l[i * j] = 1
		j += 1
	i += 1
	while i < N and l[i] == 1:
		i += 1

print len(filter(lambda i: l[i] == 0 and sum(l[j] for j in rshift(i)) == 0, range(2, N)))