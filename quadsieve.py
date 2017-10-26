# -*- coding: utf-8 -*-
'''
Created on 2015/07/12

@author: Campbell

Quadratic sieve to get prime factors 


'''
import time, numbers, sys, math
n = 15347

# get list of first 4 primes for which n has integer square root mod p
count = 0
pList = []
pCandidate = 2
while count < 4:
    if numbers.isPrime(pCandidate):
        for a in range(pCandidate):
            if (a**2)%pCandidate == n%pCandidate:
                pList.append(pCandidate)
                count+= 1
                #print pCandidate, a, a**2%pCandidate
                break
    pCandidate += 1

# construct sieve V

V = []
rootN = int(n**0.5) + 1
for x in range(100):
    V.append((x + rootN)**2 - n)

print V   
            
        
    

