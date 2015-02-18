#!/usr/bin/env python

'''
	Project Euler Problem 002 - Even Fibonacci numbers
	----------------
	Description:
		By considering the terms in the Fibonacci sequence whose values 
		do not exceed four million, find the sum of the even-valued terms.
	Solution:
		4613732
	----------------
	Haoliang Wang 01/27/2015
'''

MAX = 4000000

def fib(m):
	a, b = 0, 1
	while True:
		if a > m:
			return
		yield a
		a, b = b, a + b

print sum(filter(lambda x: not x % 2, fib(MAX)))

