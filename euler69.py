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

def getPhi(n):
    
    phi = n
    listPF = numbers.getPrimeFactors(n)
    if listPF == []:
        listPF.append(n)
    for p in listPF:
        phi = phi * (1.0 - 1.0/p)
                
    return phi 
            

if __name__=='__main__':
    #testing
    s = time.time()
    maxPhi = 0.0
    num = 10
    for x in range(2,num):
        if x%10000 == 0:
            print x, time.time() - s
       
        newPhi = getPhi(x)
        print x, newPhi
        if newPhi > maxPhi:
            maxPhi = newPhi
    
    print("maxPhi =", maxPhi)
    print("Euler 69 took %f seconds" % (time.time() - s))

sys.exit(1)

