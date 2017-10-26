'''
Created on 2015/06/02

@author: Campbell

Euler 63 - 

The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?


'''
import time, numbers, sys, iccnumbers, collections, itertools

tic = time.clock()

matchList = list()
for n in range(1,10):
        for i in range(300):
                if len(str(n**i)) == i:
                        matchList.append([n,i,n**i])
                        

print matchList, "length", len(matchList)
print("Time elapsed =", time.clock() - tic)

sys.exit(1)

