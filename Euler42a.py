'''
Created on 2 Jan 2012

@author: Campbell

Euler 42 - find 0-9 pandigitals that have divisible substrings
'''
import time
import permutations
import isprime

tic = time.clock()

inNum = "1406357289"
inlist = [inNum]
numList = [n for n in inlist if not int(n[7:])%17
           if not int(n[6:9])%13 
           if not int(n[5:8])%11
           if not int(n[4:7])%7
           if not int(n[3:6])%5
           if not int(n[2:5])%3
           if not int(n[1:4])%2]


print (len(numList))
    
    
print("Time elapsed =", time.clock() - tic)

