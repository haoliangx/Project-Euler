#!/usr/bin/env python

n = 1000000

def nextCollatz(n):
    return n if n == 1 \
        else n / 2 if n % 2 == 0 \
        else 3 * n + 1

def collatzLen(n, d):
    if n not in d:
        d[n] = 1 + collatzLen(nextCollatz(n),d)
    return d[n]

d = {1: 1}
max_i = 1
max_len = 1
for i in range(2, n):
    my_len = collatzLen(i,d)
    if my_len > max_len:
        max_i = i
        max_len = my_len
print max_i