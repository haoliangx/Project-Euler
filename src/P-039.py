#!/usr/bin/env python

'''
	Project Euler Problem 039 - Integer right triangles
	----------------
	Description:
		If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
		For which value of p <= 1000, is the number of solutions maximised?
	Solution:
		
	----------------
	Haoliang Wang 02/06/2015
'''

m = {}

for p in range(3, 1001):
	s = 0
	for a in range(1, p / 3 + 1):
		for b in range(a, p / 2 + 1):
			if (p - a - b) ** 2 == a ** 2 + b ** 2:
				s += 1
	m[p] = s

print max(m, key = lambda x: m[x])