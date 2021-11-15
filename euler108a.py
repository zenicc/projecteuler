"""
Created on 13 Aug 2020
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

https://www.cut-the-knot.org/arithmetic/ShortEquationInReciprocals.shtml explains my approach

If n = kms then a  = km(m + s) and b = ks(m + s)

The previous version included duplicate solutions from different factorisations of n. This attempts to to get round that.
This works but is slow - 300 secs - 108b is faster
"""

import time

import getFacts, iccnumbers


def getDioRecs(n, l):
    drList = []  # list of a,b pairs
    incList = []  # list of a or b values already known
    candList = [] # list of candidate 3 number factorisations
    # get all 3 number factorisations of n
    fList = getFacts.getFacts(n)
    fList.append([1, n])  # as my getFacts doesn't return 1 * n
    for a in fList:
        if len(a) == 2:
            a.append(1)
        if len(a) == 3:
            candList.append(a)
    if len(candList) < l/3:
        return(drList)

    for a in candList:
        for b in a:
            c = a.copy()
            c.remove(b)
            d = [b, c[0], c[1]]
            f1 = d[0] * d[1] * (d[1] + d[2])
            f2 = d[0] * d[2] * (d[1] + d[2])

            if not (f1 in incList):
                incList.append(f1)
                incList.append(f2)
                drList.append([f1, f2])
    #if n == 400:
   #    drList = [[1]]*500

    return (drList)


if __name__ == '__main__':
    # testing
    st = time.time()
    limit = 4

    n = int(limit*3)
    drList = []

    while len(drList) < limit:
        if not iccnumbers.isPrime(n):
            drList = getDioRecs(n, int(limit) + 1)
            #print(n)
            #print(drList, "**********", len(drList))
            #print(incList, "**********", len(incList))
        n += 1
    print(len(drList), n-1)
    print("euler108a took %f seconds" % (time.time() - st))
