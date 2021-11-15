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

If n = kmn then a  = km(m + n) and b = kn(m + n)

"""

import time
import getFacts

if __name__ == '__main__':
    # testing
    st = time.time()

    n = 18
    drList = []
    # get all 3 number factorisations of n
    fList = getFacts.getFacts(n)
    fList.append([1, n]) # as my getFacts doesn't return 1 * n
    for a in fList:
        if len(a) == 2:
            a.append(1)
        if len(a) > 3:
            fList.remove(a)


    print(fList)

    # get all factorisation permutations needed
    for a in fList:
        if len(set(a)) == 3: # all numbers are different - so add one row with each number in turn as n
            for b in a:
                c = a.copy()
                c.remove(b)
                drList.append([b, c[0], c[1]])
        elif len(set(a)) == 2:    # 2 different numbers ie [1,1,x] or [1,x,x] - for [1,1,x] we want [1,1,x] and [x,1,1]
                                  # for [1,x,x] we only want [x,1,x]
            aSet = list(set(a))
            aSet.sort()
            if a.count(1) == 2:                         # so it is of the form [1,1,x]
                drList.append([1, 1, aSet[1]])          # [1,1,x]
                drList.append([aSet[1], 1, 1])          # [x,1,1]
            else:                                       # it is of the form [1,x,x]
                drList.append([aSet[1], 1, aSet[1]])


        else:                                           # only one number - the cube root
            drList.append([a[0], a[0], a[0]])

    print(n)
    for a in drList:
        f1 = a[0] * a[1] * (a[1] + a[2])
        f2 = a[0] * a[2] * (a[1] + a[2])
        print(a)
        print(f1, f2, 1 / (1 / f1 + 1 / f2))
    print(drList)

    print("euler107 took %f seconds" % (time.time() - st))
