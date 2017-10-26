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
from collections import defaultdict
from itertools import count
from operator import mul

def gcd(a, b):
    while a != 0: a, b = b % a, a
    return b
def lcm(a, b): return a * b / gcd(a, b)
primes_cache, prime_jumps = [], defaultdict(list)
def primes():
    prime = 1
    for i in count():
        if i < len(primes_cache): prime = primes_cache[i]
        else:
            prime += 1
            while prime in prime_jumps:
                for skip in prime_jumps[prime]:
                    prime_jumps[prime + skip] += [skip]
                del prime_jumps[prime]
                prime += 1
            prime_jumps[prime + prime] += [prime]
            primes_cache.append(prime)
        yield prime
def factorize(n):
    for prime in primes():
        if prime > n: return
        exponent = 0
        while n % prime == 0:
            exponent, n = exponent + 1, n / prime
        if exponent != 0:
            yield prime, exponent
def getPhi(n):
    return int(reduce(mul, (1 - 1.0 / p for p, exp in factorize(n)), n))
            

if __name__=='__main__':
    #testing
    s = time.time()
    maxPhi = 0.0
    for x in range(2,10):
        newPhi = getPhi(x)
        print(x, newPhi)
        if newPhi > maxPhi:
            maxPhi = newPhi
    
    print("maxPhi =", maxPhi)
    print("Euler 69b took %f seconds" % (time.time() - s))

sys.exit(1)

