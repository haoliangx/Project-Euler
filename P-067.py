#!/usr/bin/env python

'''
	Project Euler Problem 067 - Maximum path sum II
	----------------
	Description:
		Find the maximum total from top to bottom of the triangle below:
	Solution:
		7273
	----------------
	Haoliang Wang 01/29/2015
'''

# p-67 data
data = []
with open('data-p067', 'r') as f:
	for line in reversed(f.readlines()):
		data.append([int(n) for n in line.strip().split(' ')])

# dynamic programming approach
s = [data[0], ]

for k in range(1, len(data)):
	s.append(
		[
			max(s[k - 1][i], s[k - 1][i + 1]) + data[k][i] for i in range(len(data[k]))
		]
	)

print s[len(data) - 1][0]