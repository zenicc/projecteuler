'''
Created on 3 Jan 2012

@author: Campbell

Euler 48 - find last 10 digits of 1**1 + 2**2 + 3**3 + ... + 1000**1000
'''
import time
from numbers import isPrime, getPrimeFactors 

tic = time.clock()

total=0
for i in range(1,11):
    total += i**i

print("i = ", i)
print(str(total)[-10:])

print("Time elapsed =", time.clock() - tic)

