# -*- coding: utf-8 -*-
'''
Created on 2015/09/21

@author: Campbell

Ordered Fractions

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator of the fraction
immediately to the left of 3/7.

'''
#import time, numbers, sys, iccnumbers, collections, itertools
import time, sys, numbers

def getFrac(n):
# return the fraction that is nearest to 3/7 (but lower if not exact) for the n passed.
# e.g. if n = 15, then 6 is returned
                
    return n*3/7
            

if __name__=='__main__':
    #testing
    s = time.time()
    num = 1000001
    maxND = 0.0
    lim = 3.0/7
        
    for d in range(999995,num):
        n = getFrac(d)
        candND = 1.0*n/d
        print   n, d, candND
        if candND > maxND and candND < lim:
            maxND = candND
            maxN = n
            maxD = d
            print   maxN, maxD, candND
    print("Euler 71 took %f seconds" % (time.time() - s))

sys.exit(1)

