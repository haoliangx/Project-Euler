#!/usr/bin/env python

'''
	Project Euler Problem 018 - Maximum path sum I
	----------------
	Description:
		Find the maximum total from top to bottom of the triangle below:
	Solution:
		1074
	----------------
	Haoliang Wang 01/29/2015
'''

# p-18 data
data = [
	[ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23, ],
	[63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31, ],
	[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48, ],
	[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57, ],
	[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14, ],
	[41, 48, 72, 33, 47, 32, 37, 16, 94, 29, ],
	[41, 41, 26, 56, 83, 40, 80, 70, 33, ],
	[99, 65,  4, 28,  6, 16, 70, 92, ],
	[88,  2, 77, 73,  7, 63, 67, ],
	[19,  1, 23, 75,  3, 34, ],
	[20,  4, 82, 47, 65, ],
	[18, 35, 87,  1, ],
	[17, 47, 82, ],
	[95, 64, ],
	[75, ],
]

# dynamic programming approach
s = [data[0], ]

for k in range(1, len(data)):
	s.append(
		[
			max(s[k - 1][i], s[k - 1][i + 1]) + data[k][i] for i in range(len(data[k]))
		]
	)

print s[len(data) - 1][0]