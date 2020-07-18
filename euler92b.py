'''
Created on 25 Nov 2019
@author: Campbell

A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?

'''

import time, csv, math
from getprimes import getPrimes
from getFacts import getFacts
from iccnumbers import gcd

import numpy

s = time.time()
count = 0
lim = 10000000
numlist = [0]*lim
for num in range(1, 568):
    n = num
    while n not in [1, 89]:
        tot = 0
        for x in [int(i) for i in str(n)]:
            tot += x*x
        if numlist[tot] > 0:
            numlist[num] = numlist[tot]
            n = numlist[num]
        else:
            n = tot
    if numlist[num] == 0:
        numlist[num] = n
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    for f in range(10):
                        for g in range(10):
                            n = a*1000000+b*100000+c*10000+d*1000+e*100+f*10+g
                            if n > 567:
                                numlist[n] = numlist[a*a + b*b + c*c + d*d + e*e + f*f +g*g]
print(numlist.count(0))
print(numlist.count(1))
print(numlist.count(89))
print("euler92 took %f seconds" % (time.time() - s))