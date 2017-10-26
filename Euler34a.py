'''
Created on 27 Dec 2011

@author: Campbell

Euler 34 - returns total of all numbers which are palindromic in both decimal
and binary formats
'''
import time
from ispalindrome import ispalindrome

tic = time.clock()

numList = list(range(1,1000000,2))
binList = [bin(n)[2:] for n in numList if ispalindrome(bin(n)[2:])]


decList = [n for n in numList if ispalindrome(str(n))
           if bin(n)[2:] in binList]


print (decList)
print (sum(decList))
    
print("Time elapsed =", time.clock() - tic)

