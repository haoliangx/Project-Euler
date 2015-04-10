#!/usr/bin/env python

'''
	Project Euler Problem 016 - Power digit sum
	----------------
	Description:
		What is the sum of the digits of the number 2^1000?
	Solution:
		1366
	----------------
	Haoliang Wang 01/29/2015
'''

print sum([int(i) for i in str(2 ** 1000)])


