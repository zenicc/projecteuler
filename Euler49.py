'''
Created on 8 Jan 2012

@author: Campbell

Euler 49 - find 4 digit primes which are permutations and form a 3 number
arithmetic sequence
'''
import time
from numbers import isPrime, getPrimeFactors, isPermutation 

tic = time.clock()

primeList = []
#get all primes 
for i in range(1001,10000):
    if isPrime(i):
        primeList.append(i)

for a in range(1, len(primeList)):
    for b in range(a+1, a + int((len(primeList) - a)/2) + 1):
        if isPermutation(primeList[a], primeList[b]):
            if isPrime(primeList[b] + (primeList[b] - primeList[a])) and \
               isPermutation(primeList[a], primeList[b] + (primeList[b] - primeList[a])):
                    print(primeList[a], primeList[b], primeList[b] + (primeList[b] - primeList[a]))

print("Time elapsed =", time.clock() - tic)

