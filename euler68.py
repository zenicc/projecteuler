# -*- coding: utf-8 -*-
'''
Created on 2015/06/17

@author: Campbell

Euler 68 - 

Euler's Totient function, φ(n) [sometimes called the phi function],
is used to determine the number of numbers less than n which are
relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are
all less than nine and relatively prime to nine, φ(9)=6.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

'''
#import time, numbers, sys, iccnumbers, collections, itertools
import time, sys, numbers

def getRelativePrimes(n):

    listRP = []
    if numbers.isPrime(n):
        for p in range(1,n):
            listRP.append(p)
        return listRP
    
    for a in range(1,n):
        noRelPrime = True
        lim = a+1
        for b in range(2,lim):
            #print n,a,b
            if (a%b == 0 and
                n%b == 0):
                noRelPrime = False
                break
        if noRelPrime == True:
            listRP.append(a)
            
    return listRP 
            

if __name__=='__main__':
    #testing
    s = time.time()
    maxRatio = 0.0
    for x in range(2,1001):
        RP = getRelativePrimes(x)
        ratio = x*1.0/len(RP)
        if ratio > maxRatio:
            maxRatio = ratio        
            print x, RP, x*1.0/len(RP)
    
    print("Euler 68 took %f seconds" % (time.time() - s))

sys.exit(1)

