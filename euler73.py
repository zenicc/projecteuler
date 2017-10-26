# -*- coding: utf-8 -*-
'''
Created on 2015/11/09

@author: Campbell



Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?



'''
#import time, numbers, sys, iccnumbers, collections, itertools
import time, sys, numbers


if __name__=='__main__':
    #testing
    s = time.time()
    upperLimit = 1.0/2.0
    lowerLimit = 1.0/3.0
    num = 12000
    tot = 0
    fractList = []
    
    for d in range(2,num+1):
        lower = d/3
        upper = d/2 + 1
        #print d, lower, upper
        for n in range(lower,upper):
            if numbers.gcd(n,d) == 1:
                cand = 1.0*n/d
                if cand < upperLimit and cand > lowerLimit:
                    #print n,"/",d
                    tot = tot + 1
    print "Total = ",tot
    print("Euler 73 took %f seconds" % (time.time() - s))

sys.exit(1)

