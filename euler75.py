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
import time, sys
'''
def getFactSumXXX(n):
# Return the sum of the factorials of each digit of n
# e.g. if n = 24, then 2! + 4! = 26 is returned
                
    numStr = str(n)
    tot = 0
    for x in range(len(numStr)):
        tot += math.factorial(int(numStr[x]))
    return tot

def getFactSum(n):
# Return the sum of the factorials of each digit of n
# e.g. if n = 24, then 2! + 4! = 26 is returned
                
    tot = 0
    while n > 9:
        rem = n%(10*(n/10))
        n = n/10
        tot += math.factorial(rem)
    return tot + math.factorial(n)
            
'''
if __name__=='__main__':
    #testing
    s = time.time()
    lim = 10000
    aLim = lim/4
    bLim = lim/2
    cntList = [0]*(lim + 1)
    
    for a in range(3,aLim):
        bLoop = True
        b=a+1
        while bLoop:
            cSquared = a**2 + b**2
            c = cSquared**0.5
            if c == int(c):
                L = int(a+b+c)
                if L > lim:
                    break
                else:
                    #print a,b,c,a+b+c
                    cntList[L] +=1
            #print "loop ", a,b,c
            if ((c+1)**2 - c**2) > a**2:
                #print "break loop ", a,b,c
                bLoop = False
            b +=1
    print cntList.count(1)

        
    print("Euler 75 took %f seconds" % (time.time() - s))

sys.exit(1)
