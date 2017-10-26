'''
Created on 2 Jan 2012

@author: Campbell

Euler 46 - find exception to Goldbach Conjecture - p = p + 2 * x**2


'''
import time
from isprime import isprime 

tic = time.clock()

for a in range(9,6000,2):
    if not isprime(a):
        gold = False
        for n in range(1,int((0.5*a)**0.5)+1):
            if isprime(a - 2*n**2):
                gold = True
                break
        if not gold:
            print(a)

print("Time elapsed =", time.clock() - tic)

