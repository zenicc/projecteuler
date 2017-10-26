# -*- coding: utf-8 -*-
'''
Created on 2015/09/21

@author: Campbell

Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive
numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all
less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 10**7, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.


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
        listPF = numbers.getPrimeFactorsList(n, prList)
        phi = n*1.0
        for p in listPF:
            phi = phi * (1.0 - 1.0/p)
        pList[n] = int(phi)
                
    return pList
            

if __name__=='__main__':
    #testing
    s = time.time()
    minPhi = 1000000.0
    num = 10000001
    phiList = [0]*num
    primeList = numbers.getPrimes(int(num**0.5) + 1)
    
    for x in range(2,num):
        if phiList[x] == 0:
            phiList = getPhi(x, phiList, num, primeList)
        phiRat = 1.0*x/phiList[x]
        if numbers.isPermutation(x, phiList[x]):
            if phiRat < minPhi:
                minPhi = phiRat
                print x, phiList[x]

    print("Euler 70 took %f seconds" % (time.time() - s))

sys.exit(1)

