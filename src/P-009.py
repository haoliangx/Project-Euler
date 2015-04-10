#!/usr/bin/env python

'''
	Project Euler
	Problem 009 - Special Pythagorean triplet
	Haoliang Wang
	01/28/2015
'''

'''
	Description:
		There exists exactly one Pythagorean triplet (a^2 + b^2 = c^2)
		for which a + b + c = 1000.
		Find the product abc.
		a, b, c are natural numbers
	Solution:
		31875000
'''

# a+b+c = 1000
# a^2 + b^2 = c^2
# a = (10**6 - 2000 * b) / (2000 - 2 * b)
# a , b both < c => 0 < a, b < 500

for b in range (1, 500):
	if (10**6 - 2000 * b) % (2000 - 2 * b) == 0:
		a = (10**6 - 2000 * b) / (2000 - 2 * b)
		break

c = 1000 - b - a

print a * b * c