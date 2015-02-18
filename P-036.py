#!/usr/bin/env python

'''
	Project Euler Problem 036 - Double-base palindromes
	----------------
	Description:
		Find the sum of all numbers, less than one million, 
		which are palindromic in base 10 and base 2.
	Solution:
		872187
	----------------
	Haoliang Wang 02/06/2015
'''

def is_panlindrome(n):
	return bin(n)[2:] == bin(n)[:1:-1]

s = []
for f in range(1000):
	n = int(str(f) + str(f)[::-1])
	m = int(str(f) + str(f)[-2::-1])
	if is_panlindrome(n): s.append(n)
	if is_panlindrome(m): s.append(m)

print sum(s)