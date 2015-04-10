#!/usr/bin/env python

'''
	Project Euler
	Problem 007 - 10001st prime
	Haoliang Wang
	01/28/2015
'''

'''
	Description:
		What is the 10001st prime number?
	Solution:
		104743
'''

from math import sqrt

n = 10001

nsqrt = 1000000L

l = [0] * nsqrt
i = 2
while i < nsqrt:
	j = 2
	while i * j < nsqrt:
		l[i * j] = 1
		j += 1
	i += 1
	while i < nsqrt and l[i] == 1:
		i += 1

s = 0
for i in range(2, len(l)):
	if l[i] == 0:
		s += 1
	if s == n:
		print i
		break
