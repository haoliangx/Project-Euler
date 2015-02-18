#!/usr/bin/env python

'''
	Project Euler
	Problem 005 - Smallest multiple
	Haoliang Wang
	01/27/2015
'''

'''
	Description:
		What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
	Solution:
		232792560
'''

n = 20

# Simple prime generator
# p = {2 : 0, 3 : 0, 5 : 0, 7 : 0, 11 : 0, 13 : 0, 17 : 0, 19 : 0, }
def is_prime(num):
	if num == 0 or num == 1:
		return False
	for x in range(2, num):
		if num % x == 0:
			return False
	else:
		return True
p = dict((i, 0) for i in filter(is_prime, range(n)))

l = range(1, n + 1)

for i in range(0, n):
	for pn in p.keys():
		if l[i] % pn == 0:
			for j in range(i, n):
				l[j] = l[j] / pn if l[j] % pn == 0 else l[j]
			p[pn] += 1

s = 1
for i in p.keys():
	s *= i ** p[i]

print s