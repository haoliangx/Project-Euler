#!/usr/bin/env python

'''
	Project Euler Problem 033 - Digit cancelling fractions
	----------------
	Description:
		There are exactly four non-trivial examples of this 
		type of fraction, less than one in value, and containing 
		two digits in the numerator and denominator.

		If the product of these four fractions is given in its 
		lowest common terms, find the value of the denominator.
	Solution:
		100
	----------------
	Haoliang Wang 01/30/2015
'''
from fractions import Fraction
from operator import mul

s = []

for k in xrange(1, 10):
	for x in xrange(1, 10):
		for y in xrange(x + 1, 10):
			if (k * 10 + x) * y == (k * 10 + y) * x or		\
				(x * 10 + k) * y == (k * 10 + y) * x or		\
				(k * 10 + x) * y == (y * 10 + k) * x or 	\
				(x * 10 + k) * y == (y * 10 + k) * x :
				s.append(Fraction(x, y))

print reduce(mul, s).denominator