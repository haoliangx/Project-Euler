#!/usr/bin/env python

'''
	Project Euler Problem 026 - Reciprocal cycles
	----------------
	Description:
		Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
	Solution:
		983
	----------------
	Haoliang Wang 02/04/2015
'''

def num_decimals(n):
	t = n
	while not t % 2:
		t /= 2
	while not t % 5:
		t /= 5
	if t == 1:
		return 0
	i = 1
	while True:
		if not (10 ** i - 1) % t:
			return i
		i += 1

k = 1
m = 0
for i in range(1, 1000):
	if m < num_decimals(i):
		k = i
		m = num_decimals(i)

print k
			

