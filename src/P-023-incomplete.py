#!/usr/bin/env python

'''
	Project Euler Problem 023 - Non-abundant sums
	----------------
	Description:
		Find the sum of all the positive integers which cannot be written as 
		the sum of two abundant numbers.
	Solution:
		
	----------------
	Haoliang Wang 01/30/2015
'''

MAX = 28123

l = {}
def d(n):
	if n not in l:
		l[n] = sum([m + n / m for m in range(1, int(n ** 0.5) + 1) if n % m == 0]) - n
	return l[n]

'''
for i in range(MAX):
	d(i)

s = 0
for a in range(MAX):
	print '%d' % a
	for b in range(MAX):
		if a + b < MAX:
			if d(a) > a and d(b) > b:
				s += a + b
		else:
			break

print sum(range(MAX)) - s
'''

abundants = set(i for i in range(1,28124) if d(i) > i)

def abundantsum(i):
	return any(i-a in abundants for a in abundants)

print sum(i for i in range(1,28124) if not abundantsum(i))
