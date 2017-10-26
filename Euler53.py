'''
Created on 16 Dec 2012

@author: Campbell

Euler 53 - How many, not necessarily distinct,
values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?
'''
import time
from numbers import comb

tic = time.clock()

limit = 1000000
num = 100
count = 0

for n in range(0, num+1):
    r = 0
    found = False
    while not found:
        #print("n = ",n,": r = ", r, ": c = ", comb(n,r))
        if comb(n,r) > limit:
           count = count + (n - 2*r + 1)
           found = True
        else:
            r = r + 1
            if r > n:
                found = True

print("count = ", count)
print("Time elapsed =", time.clock() - tic)
