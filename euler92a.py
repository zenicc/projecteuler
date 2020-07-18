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
lim = 568
numlist = [0]*lim
maxsteps = 0
for num in range(1,lim):
    n = num
    steps = 0
    while n not in [1,89]:
        tot = 0
        for x in [int(i) for i in str(n)]:
            tot += x*x
        if numlist[tot] > 0:
            numlist[num] = numlist[tot]
            n = numlist[num]
        else:
            n = tot
            steps += 1
    if steps > maxsteps:
        maxsteps = steps
    if numlist[num] == 0:
        numlist[num] = n
print(numlist.count(89))
print(maxsteps)
print("euler92 took %f seconds" % (time.time() - s))