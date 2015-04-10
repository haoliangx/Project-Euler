#!/usr/bin/env python

'''
	Project Euler Problem 015 - Lattice paths
	----------------
	Description:
		Starting in the top left corner of a 2x2 grid, and only being able 
		to move to the right and down, there are exactly 6 routes to the bottom 
		right corner. How many such routes are there through a 20x20 grid?
	Solution:
		137846528820
	----------------
	Haoliang Wang 01/29/2015
'''
from fractions import Fraction

n = 20

def choose(n, k): 
	return reduce(lambda x, y: x * y, [Fraction(n - i, i + 1) for i in range(k)], 1)

print choose(n * 2, n)


