'''
Created on 3 Jan 2012

@author: Campbell

Euler 47 - find 4 consecutive integers with 4 distinct prime factors


'''
import time
from numbers import isPrime, getPrimeFactors 

tic = time.clock()

factList = [0]
for a in range(1,20000):
    factList.append(len(getPrimeFactors(a)))
for b in range(1,20000 - 4):
    if factList[b] == 4 and \
       factList[b + 1] == 4 and \
       factList[b + 2] == 4 and \
       factList[b + 3] == 4:
        print(b)

    
print("Time elapsed =", time.clock() - tic)

