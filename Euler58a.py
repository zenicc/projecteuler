'''
Created on 18 Dec 2012

@author: Campbell

Euler 58 - what is the side length of the
square spiral for which the ratio of primes
along both diagonals first falls below 10%?
'''
import time
from isprime import isPrime

tic = time.clock()

dp = 0
da = 1
num = 1
inc = 0
ratio = 1
while ratio >= 0.1:
    inc = inc + 2
    for j in range(1,5):
        da = da + 1
        num = num + inc
        if isPrime(num):
            dp = dp + 1
    ratio = dp/da
#print(diagonals)
print(ratio)
print("length ", inc + 1)

print("Time elapsed =", time.clock() - tic)
