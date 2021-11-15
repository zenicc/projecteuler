"""
Created on 22 Aug 2020
@author: Campbell
In the following equation x, y, and n are positive integers.

1/x + 1/y = 1/n

It can be verified that when n = 1260 there are 113 distinct solutions and this is the least value of n

for which the total number of distinct solutions exceeds one hundred.

What is the least value of

for which the number of distinct solutions exceeds four million?

NOTE: This problem is a much more difficult version of Problem 108 and as it is well beyond the limitations of a brute force approach it requires a clever implementation.

**********************************************************************
My Note:

There will be a solution for each k that divides into n**2 - proof is in solution forum.

From Sloane's A018892:

If n = (p1^a1)(p2^a2)...(pt^at), where each p is a prime
a(n) = ((2*a1 + 1)(2*a2 + 1) ... (2*at + 1) + 1)/2   where a(n) returns the number of divisors of n**2

We want ((2 a1 + 1)(2 a2 + 1) ... (2 at + 1) + 1)/2 > 4000000
so, (2 a1 + 1)(2 a2 + 1) ... (2 at + 1) >= 8000000

Start by setting the exponential values (a1, a2 etc.) to 1 for the first y primes where y is the lowest value such that 3**y (ie (2*1 + 1)**y) > 8000000.
Then try removing the highest prime and increasing other lower prime exponentials until you get the lowest product such that
the a(n) function still returns a value greater than 8000000.

"""

import time

import iccnumbers, numpy


def getPrimeExp(l):
    # returns the value where a list of the exponential values passed  are applied to the prime components
    # eg [0,2,1] would return (2**0)*(3**2)*(5**1) = 45
    tot = 1
    pList = iccnumbers.getPrimesCount(len(l))
    for n in range(len(l)):
        tot *= pList[n] ** l[n]

    return (tot)

def getN(l):
    # returns the value of the list where a 1 counts as 3, 2 as 5, 3 as 7 etc.
    tot = 1

    for n in range(len(l)):
        tot *= (l[n] * 2) + 1

    return ((tot + 1)/2)


if __name__ == '__main__':
    # testing
    st = time.time()

    limit = 4000000

    s = 1
    while limit >= ((3 ** s) + 1) / 2:
        s += 1
    print(s, f"{((3 ** s) + 1) / 2:,}")

#    nextDown = (((3 ** s) + 1) / 2) / s
#    print("limit/nextDown", limit / nextDown,
#          " - need to increase lower values until this value is just exceeded - ie make the first value 5 - so the total above might be 5*(3**(s-1)) and the powerList below would be [2,1,1,...] ")
#    print("nextDown", f"{nextDown:,}")

    powerList = [1] * (s)

    divs = getPrimeExp(powerList)  # this gives the number of divisors
    print(f"{getN(powerList):,}")
    print(f"{divs:,}")
    print("-------------------")

    del powerList[-1]

    divs = getPrimeExp(powerList)  # this gives the number of divisors
    print(f"{getN(powerList):,}")
    print(f"{divs:,}")
    print("-------------------")

    powerList[0] = 2
    print("powerList[0] = 2")

    divs = getPrimeExp(powerList)  # this gives the number of divisors
    print(f"{getN(powerList):,}")
    print(f"{divs:,}")
    print("-------------------")

    powerList[0] = 3
    print("powerList[0] = 3")

    divs = getPrimeExp(powerList)  # this gives the number of divisors
    print(f"{getN(powerList):,}")
    print(f"{divs:,}")
    print("-------------------")

    powerList[0] = 2
    powerList[1] = 2
    print("powerList[0] = 2")
    print("powerList[1] = 2")

    divs = getPrimeExp(powerList)  # this gives the number of divisors
    print(f"{getN(powerList):,}")
    print(f"{divs:,}")
    print("-------------------")

    del powerList[-1]

    powerList[0] = 2
    powerList[1] = 2
    print("powerList[0] = 2")
    print("powerList[1] = 2")

    divs = getPrimeExp(powerList)  # this gives the number of divisors
    print(f"{getN(powerList):,}")
    print(f"{divs:,}")
    print("-------------------")

    powerList[0] = 3
    powerList[1] = 2
    print("powerList[0] = 3")
    print("powerList[1] = 2")

    divs = getPrimeExp(powerList)  # this gives the number of divisors
    print(f"{getN(powerList):,}")
    print(f"{divs:,}")
    print("-------------------")

    powerList[0] = 3
    powerList[1] = 3
    print("powerList[0] = 3")
    print("powerList[1] = 3")
    print(powerList)

    divs = getPrimeExp(powerList)  # this gives the number of divisors
    print(f"{getN(powerList):,}")
    print(f"{divs:,}")
    print("-------------------")

    powerList[0] = 4
    powerList[1] = 2
    print("powerList[0] = 4")
    print("powerList[1] = 2")

    divs = getPrimeExp(powerList)  # this gives the number of divisors
    print(f"{getN(powerList):,}")
    print(f"{divs:,}")
    print("-------------------")

    powerList[0] = 5
    powerList[1] = 2
    print("powerList[0] = 5")
    print("powerList[1] = 2")

    divs = getPrimeExp(powerList)  # this gives the number of divisors
    print(f"{getN(powerList):,}")
    print(f"{divs:,}")
    print("-------------------")

    powerList[0] = 3
    powerList[1] = 2
    powerList[2] = 2
    print("powerList[0] = 3")
    print("powerList[1] = 2")
    print("powerList[2] = 2")

    divs = getPrimeExp(powerList)  # this gives the number of divisors
    print(f"{getN(powerList):,}")
    print(f"{divs:,}")
    print("-------------------")







    print("euler110 took %f seconds" % (time.time() - st))
