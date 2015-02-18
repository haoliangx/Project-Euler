#!/usr/bin/env python

'''
	Project Euler
	Problem 004 - Largest palindrome product
	Haoliang Wang
	01/27/2015
'''

'''
	Description:
		Find the largest palindrome made from the product of two 3-digit numbers.
	Solution:
		906609
'''

def is_palindrome(n):
	return str(n) == str(n)[::-1]

s = 0

for i in reversed(xrange(100, 1000)):
	for j in reversed(xrange(100, 1000)):
		n = i * j
		if n < s:
			break
		elif is_palindrome(n):
			s = n if n > s else s

print s