# -*- coding: utf-8 -*-
'''
Created on 2015/07/02

@author: Campbell

Euler 69 - 

Euler's Totient function, φ(n) [sometimes called the phi function],
is used to determine the number of numbers less than n which are
relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are
all less than nine and relatively prime to nine, φ(9)=6.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

'''
#import time, numbers, sys, iccnumbers, collections, itertools
import time, sys, numbers

def getPhi(n, pList, num, prList):
    
    
    if n in prList:
        pList[n] = int(n * (1.0 - 1.0/n))
        x = 2
        while n*x < num and x < n:
            pList[n*x] = pList[n]*pList[x]
            x += 1
    else:
        listPF = numbers.getPrimeFactors(n)
        phi = n*1.0
        for p in listPF:
            phi = phi * (1.0 - 1.0/p)
        pList[n] = int(phi)
                
    return pList
            

if __name__=='__main__':
    #testing
    s = time.time()
    maxPhi = 0.0
    maxX = 0
    num = 1000001
    phiList = [0]*num
    primeList = numbers.getPrimes(num)
    
    for x in range(2,num):
        if phiList[x] == 0:
            phiList = getPhi(x, phiList, num, primeList)
        phiRat = 1.0*x/phiList[x]
        if phiRat > maxPhi:
            maxPhi = phiRat
            maxX = x
            print maxX, phiList[x], maxPhi

    #for i in range(0,num,10):
    #    print(phiList[i:i+10])
    print "maxX =", maxX
    print "maxPhi =", maxPhi
    #print len(primeList)
    print("Euler 69d took %f seconds" % (time.time() - s))

sys.exit(1)

