"""
Created on 22 Aug 2020
@author: Campbell

In the following equation x, y, and n are positive integers.

1/x  +  1/y  =  1/n

For n = 4 there are exactly three distinct solutions:

1/5  +  1/20  =  1/4
1/6  +  1/12  =  1/4
1/8  +  1/8   =  1/4

What is the least value of n for which the number of distinct solutions exceeds one-thousand?

NOTE: This problem is an easier version of Problem 110; it is strongly advised that you solve this one first.

**********************************************************************
My Note:

There will be a solution for each k that divides into n**2 - proof is in solution forum.

From Sloane's A018892:

If n = (p1^a1)(p2^a2)...(pt^at), where each p is a prime
a(n) = ((2*a1 + 1)(2*a2 + 1) ... (2*at + 1) + 1)/2   where a(n) returns the number of divisors of n**2

We want ((2 a1 + 1)(2 a2 + 1) ... (2 at + 1) + 1)/2 > 1000
so, (2 a1 + 1)(2 a2 + 1) ... (2 at + 1) >= 2000

Start by setting the exponential values (a1, a2 etc.) to 1 for the first y primes where y is the lowest value such that 3**y (ie (2*1 + 1)**y) > 2000.
Then try removing the highest prime and increasing other lower prime exponentials until you get the lowest product such that
the a(n) function still returns a value greater than 2000.

"""

import time

import iccnumbers, numpy

def getPrimeExp(l):
    # returns the value where a list of the exponential values passed  are applied to the prime components
    # eg [0,2,1] would return (2**0)*(3**2)*(5**1)
    tot = 1
    pList = iccnumbers.getPrimesCount(len(l))
    for n in range(len(l)):
        tot *= pList[n]**l[n]

    return(tot)



if __name__ == '__main__':
    # testing
    st = time.time()
    limit = 100

    n = 2
    l = 3
    drList = []

    while l < limit:
        l *= 3
        n += 1
    print(l, n-1)

    powerList = [1]*(n-1)

    prod = getPrimeExp(powerList)
    print(powerList)
    print(prod)
    print("euler108b took %f seconds" % (time.time() - st))
