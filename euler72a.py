# -*- coding: utf-8 -*-
'''
Created on 2015/09/21

@author: Campbell

Counting Fractions

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1,
it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?


'''
#import time, numbers, sys, iccnumbers, collections, itertools
import time, sys, numbers, operator

def sieve(s,n=None):
    if not n:
        n = s
        s = 2
    sieve = [True] * n
    for i in (i for i in range(3,int(n**0.5)+1,2) if sieve[i]):
        sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return ([2] if s <= 2 else []) + [i for i in range(2*(s//2)+1,n,2) if sieve[i]]

s = time.time()
primes = sieve(10**6)

totients = list(range(10**6 + 1))
for p in primes:
    totients[p::p] = map(operator.mul,totients[p::p],[1-1/p]*(10**6//p))
print(int(sum(totients)) - 1)
print("Euler 72a took %f seconds" % (time.time() - s))
            
'''
if __name__=='__main__':
    #testing
    s = time.time()
    tot = 0
    num = 1000000
    phiList = [0]*(num + 1)
    primeList = numbers.getPrimes(int(num**0.5) + 1)
    
    for x in range(2,num + 1):
        if phiList[x] == 0:
            phiList = getPhi(x, phiList, num, primeList)
        tot += phiList[x]
    #print phiList
    print "tot =", tot
    print("Euler 72 took %f seconds" % (time.time() - s))
'''
sys.exit(1)

