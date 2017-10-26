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
        x = 0
        while n*prList[x] < num and prList[x] < n:
            pList[n*prList[x]] = pList[n]*pList[prList[x]]
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
    num = 100000
    phiList = [0]*num
    primeList = numbers.getPrimes(num)
    
    for x in range(2,num):
        if phiList[x] == 0:
            phiList = getPhi(x, phiList, num, primeList)
            #print x, phiList[x]
            if phiList[x] > maxPhi:
                maxPhi = phiList[x]
                maxX = x

    #for i in range(0,num,10):
    #    print(phiList[i:i+10])
    print "maxX =", maxX
    print "maxPhi =", maxPhi
    #print len(primeList)
    print("Euler 69 took %f seconds" % (time.time() - s))

sys.exit(1)

