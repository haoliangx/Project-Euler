#!/usr/bin/env python

'''
	Project Euler Problem 025 - 1000-digit Fibonacci number
	----------------
	Description:
		What is the first term in the Fibonacci sequence to contain 1000 digits?
	Solution:
		2783915460
	----------------
	Haoliang Wang 02/03/2015
'''

N = 1000

def fib():
	x, y = 1, 1
	while True:
		yield x
		x, y = y, x + y

s = 1
for n in fib():
	if len(str(n)) >= N:
		print s
		break
	else:
		s += 1