'''
Created on 17 Dec 2012

@author: Campbell

Euler 56 - Considering natural numbers of the form,
a**b, where a, b < 100, what is the maximum digital sum?
'''
import time
from ispalindrome import ispalindrome

tic = time.clock()

maxds = 0

for a in range(1,100):
    for b in range(1,100):
        p = a**b
        maxds = max(maxds,sum([int(c) for c in str(p)]))
        
    
print(maxds)

print("Time elapsed =", time.clock() - tic)
