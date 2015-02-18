#!/usr/bin/env python

'''
	Project Euler Problem 028 - Number spiral diagonals
	----------------
	Description:
		Starting with the number 1 and moving to the right
		in a clockwise direction a 5 by 5 spiral
		What is the sum of the numbers on the diagonals in 
		a 1001 by 1001 spiral formed in the same way?
	Solution:
		669171001
	----------------
	Haoliang Wang 02/04/2015
'''

N = 1001

def sq_sum(n):
	return n * (n + 1) * (2 * n + 1) / 6

print sq_sum(N) + 8 * sq_sum((N - 1) / 2) + 1500