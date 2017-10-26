'''
Created on 14 Dec 2012

@author: Campbell

Euler 52 - Find the smallest positive integer, x,
such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''
import time
from numbers import isPermutation

tic = time.clock()

n = 10
found = False
while not found:
    if isPermutation(n, 2*n) and \
       isPermutation(n, 3*n) and \
       isPermutation(n, 4*n) and \
       isPermutation(n, 5*n) and \
       isPermutation(n, 6*n):
           print(n, 2*n, 3*n, 4*n, 5*n, 6*n)
           found = True
    else:
        n = n + 1

print("Time elapsed =", time.clock() - tic)
