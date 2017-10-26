'''
Created on 13 Dec 2012

@author: Campbell


'''
import time, numbers

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
            

if __name__=='__main__':
    #testing
    n=100000
    s = time.time()
    print(len(getPrimes(n)))
    print("First took %f seconds" % (time.time() - s))
    s = time.time()
    print(len(getPrimes2(n)))
    print("Second took %f seconds" % (time.time() - s))

    
