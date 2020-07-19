'''
Created on 13 Dec 2012

@author: Campbell


'''
import time, numbers
import numpy as np

def getPrimes(n):
    "return a list of all primes up to n"
 
    if n==2: return [2]
    elif n<2: return []
    lim = int(n**.5) + 1
    primeList = list(range(n+1))
    primeList[1] = 0
    for a in range(2, lim):
        if primeList[a]:
            lim2 = int(n/a) + 1
            for b in range(2, lim2):
                c = a*b
                try:
                    primeList[c] = 0
                except ValueError:
                    pass 
    return [x for x in primeList if x]


def getPrimes2(n):
    "return a list of all primes up to n"

    primeList = []
    for a in range(2, n):
        if numbers.isPrime(a):
            primeList.append(a)
    return primeList

def primesfrom2to(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)/3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

def rwh_primes2(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    correction = (n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [True] * (n/3)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      ((k*k)/3)      ::2*k]=[False]*((n/6-(k*k)/6-1)/k+1)
        sieve[(k*k+4*k-2*k*(i&1))/3::2*k]=[False]*((n/6-(k*k+4*k-2*k*(i&1))/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]

if __name__=='__main__':
    #testing
    n=1000
    s = time.time()
    print(getPrimes(n))
    print(len(getPrimes(n)))
    print("First took %f seconds" % (time.time() - s))
    #s = time.time()
    #print(len(rwh_primes2(n)))
    #print("Second took %f seconds" % (time.time() - s))

    
