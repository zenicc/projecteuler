'''
Created on 27 Dec 2011

@author: Campbell

Euler 36 - returns total of all numbers which are palindromic in both decimal
and binary formats
'''
import time

tic = time.clock()

print (sum(x for x in range(1,1000000,2) if str(x)==str(x)[::-1] \
           and bin(x)[2:]==bin(x)[2:][::-1]))
    
print("Time elapsed =", time.clock() - tic)

