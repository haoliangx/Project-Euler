#!/usr/bin/env python

'''
	Project Euler
	Problem 013 - Large sum
	Haoliang Wang
	01/28/2015
'''

'''
	Description:
		Work out the first ten digits of the sum of 
		the following one-hundred 50-digit numbers.
	Solution:
		5537376230
'''

def list_add(a, b):
	re = []
	carry = 0
	(lnum, snum) = (a, b) if len(a) > len(b) else (b, a)
	for i in range(1, len(lnum) + 1):
		try:
			d = lnum[-i] + snum[-i] + carry
		except:
			d = lnum[-i] + carry
		carry = d / 10
		re.insert(0, d % 10)
	if carry > 0:
		re.insert(0, 1)
	return re

result = [0, ]

with open('data-p013', 'r') as data:
	for line in data:
		number = [int(n) for n in line.strip()]
		result = list_add(result, number)

for i in range(10):
	print '%d' % result[i],