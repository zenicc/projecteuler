"""
Created on 28 Oct 2021
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
the a(n) function still returns a value greater than 4000000.

"""

import time

import iccnumbers, numpy


def getValueofList(l):
    # returns the value where a list of the exponential values passed  are applied to the prime components
    # eg [0,2,1] would return (2**0)*(3**2)*(5**1) = 45
    tot = 1
    pList = iccnumbers.getPrimesCount(len(l))
    for n in range(len(l)):
        tot *= pList[n] ** l[n]

    return (tot)

def getCountofDivs(l):
    # returns the value of the list where a 1 counts as 3, 2 as 5, 3 as 7 etc.
    tot = 1

    for n in range(len(l)):
        tot *= (l[n] * 2) + 1

    return ((tot + 1)/2)

def dealWithList(localList, outpowerList, candDivs, candN):
    # returns the max number of divisors and value of the associated powerList for the passed list

    divs = getCountofDivs(localList)
    n = getValueofList(localList)

    a = 2

# ******** calculate maxa = the max the first column can be to compensate for the loss of the highest prime in the previous list
    lostPrime = primeList[len(localList)]
    startn = 1
    maxpow = 1
    while maxpow < lostPrime:
        maxpow *= 2
        startn += 1

    maxa = outpowerList[0] + startn

    print("maxa ",maxa)

    for i in range(len(localList)):
        localList[i] = 1

    for al in range(1,maxa + 1):
        for bl in range(1, al + 1):
            for cl in range(1, bl + 1):
                for dl in range(1, cl + 1):
                    for el in range(1, dl + 1):
                        for fl in range(1, el + 1):
                            for gl in range(1, fl + 1):
                                for hl in range(1, gl + 1):
                                    localList[0] = al
                                    localList[1] = bl
                                    localList[2] = cl
                                    localList[3] = dl
                                    localList[4] = el
                                    localList[5] = fl
                                    localList[6] = gl
                                    localList[7] = hl
                                #print(localList)

                                divs = getCountofDivs(localList)
                                n = getValueofList(localList)
                                #print(f"{n:,}")
                                #print(f"{divs:,}")
                                #print("-------------------")
                                a += 1
                                if divs > limit:
                                    if  n < candN:
                                        outpowerList = localList.copy()
                                        candDivs = divs
                                        candN = n
                                        print(localList)
                                        print(f"{n:,}")
                                        print(f"{divs:,}")
                                        print("-------------------")
                                    break

    return(outpowerList, candDivs, candN)

if __name__ == '__main__':
    # testing
    st = time.time()

    limit = 4000000

    s = 1
    while limit >= ((3 ** s) + 1) / 2:
        s += 1
    print(s, f"{((3 ** s) + 1) / 2:,}")

    powerList = [1] * (s)
    print(powerList)

    primeList = iccnumbers.getPrimesCount(s)
    print(primeList)

    divs = getCountofDivs(powerList)  # this gives the number of divisors
    n = getValueofList(powerList)
    print(f"{n:,}")
    print(f"{divs:,}")
    print("-------------------")
    mpowerList = powerList.copy()
    mCandDivs = divs
    mCandN = n

##########################################################

    for nc in range(7):
        s -= 1
        powerList = [1] * (s)
        mpowerList, mCandDivs, mCandN = dealWithList(powerList, mpowerList, mCandDivs, mCandN)



##########################################################


    print("Final powerList = ", mpowerList)
    print("recalc n = ", getValueofList(mpowerList))
    print("Final n = ", mCandN)
    print("Final divs = ", mCandDivs)
    print("euler110 took %f seconds" % (time.time() - st))
