#!/usr/bin/env python

'''
	Project Euler Problem 031 - Coin sums
	----------------
	Description:
		Coins are 1, 2, 5, 10, 20, 50, 100, 200
		How many different ways can 2 pounds be made using any number of coins?
	Solution:
		73682
	----------------
	Haoliang Wang 02/04/2015
'''

M = 200
cv = [1, 2, 5, 10, 20, 50, 100, 200]

def recursive(level, value_left):
	s = 0
	if level > 0:
		for k in xrange(1 + value_left / cv[level]):
			s += recursive(level - 1, value_left - k * cv[level])
		return s
	elif value_left >= 0:
		return 1
	else:
		return 0

def dynamic_prog():
	matrix = {}
	for y in xrange(0, M + 1):
		matrix[y, 0] = 1
	for y in xrange(0, M + 1):
		for x in xrange(1, len(cv)):
			matrix[y, x] = 0
			if y >= cv[x]:
				matrix[y, x] += matrix[y, x - 1]
				matrix[y, x] += matrix[y - cv[x], x]
			else:
				matrix[y, x] = matrix[y, x - 1]
	return matrix[y, x]

print recursive(len(cv) - 1, M), dynamic_prog()
