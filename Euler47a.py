'''
Created on 3 Jan 2012

@author: Campbell

Euler 47 - find 4 consecutive integers with 4 distinct prime factors


'''
import time
from numbers import isPrime, getPrimeFactors 

tic = time.clock()

factList = [0,0,0,0]
for a in range(1,200000):
    factList.pop(0)
    factList.append(len(getPrimeFactors(a)))
    if factList[0] == 4 and \
       factList[1] == 4 and \
       factList[2] == 4 and \
       factList[3] == 4:
        print(a - 3)
        break

    
print("Time elapsed =", time.clock() - tic)

