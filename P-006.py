#!/usr/bin/env python

'''
	Project Euler
	Problem 006 - Sum square difference
	Haoliang Wang
	01/28/2015
'''

'''
	Description:
		Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
	Solution:
		25164150
'''

n = 100

sum_square = (n*(n+1)/2)**2
square_sum = n*(n+1)*(2*n + 1) / 6

print sum_square - square_sum