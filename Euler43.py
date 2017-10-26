'''
Created on 2 Jan 2012

@author: Campbell

Euler 43 - Find the sum of all 0 to 9 pandigital numbers with divisible
substrings.


'''
import time
from permutations import anagram


tic = time.clock()

inNum = "0123456789"
numList = [n for n in anagram(inNum) if int(n[7:])%17 == 0
           if int(n[6:9])%13 == 0
           if int(n[5:8])%11 == 0
           if int(n[4:7])%7 == 0
           if int(n[3:6])%5 == 0
           if int(n[2:5])%3 == 0
           if int(n[1:4])%2 == 0]


print (numList)
print (sum([int(n) for n in numList]))
    
    
print("Time elapsed =", time.clock() - tic)

