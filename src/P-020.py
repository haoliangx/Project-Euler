#!/usr/bin/env python

'''
	Project Euler Problem 020 - Factorial digit sum
	----------------
	Description:
		Find the sum of the digits in the number 100!
	Solution:
		648
	----------------
	Haoliang Wang 01/29/2015
'''
from math import factorial

print sum([int(i) for i in str(factorial(100))])