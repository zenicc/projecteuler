'''
Created on 30 Dec 2011

@author: Campbell

Euler 40 - find largest pandigital prime
'''
import time
import permutations
import isprime

tic = time.clock()

inNum = "1234567"
numList = [n for n in permutations.anagram(inNum) if isprime.isprime(int(n))]
numList.sort(reverse=True)


print (numList[0])
    
    
print("Time elapsed =", time.clock() - tic)

