# -*- coding: utf-8 -*-
'''
Created on 2016/08/16

@author: Campbell



It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?


'''
import time, sys, numbers


if __name__=='__main__':
    #testing
    s = time.time()
    lim = 1500000
    nLim = int((-6 + (36 - (16 * (2 - lim)))**0.5)/8)+1
    cntList = [0]*(lim + 1)
    
    for n in range(1,nLim):
        for m in range(n+1, int((-2 + (4*n*n + 8*lim)**0.5)/4)+1,2):
            if numbers.gcd(m,n) == 1:
                #a = m*m - n*n
                #b = 2*m*n
                #c = m*m + n*n
                #l = a+b+c
                l = 2*m*(m+n)
                lc = l
                mult = 2
                while lc <= lim:
                    cntList[lc] +=1
                    lc = l*mult
                    mult += 1
                    
                #print a,b,c,l,m,n
        
    print cntList.count(1)

        
    print("Euler 75 took %f seconds" % (time.time() - s))

sys.exit(1)
