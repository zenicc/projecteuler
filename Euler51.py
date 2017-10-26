'''
Created on 14 Dec 2012

@author: Campbell

Euler 51 - Find the smallest prime which, by replacing part of the number
(not necessarily adjacent digits) with the same digit, is part of an eight
prime value family.
'''
import time, numbers, sys

tic = time.clock()

numStr=["0","1","2","3","4","5","6","7","8","9"]
n = 1000000
pList = numbers.getPrimes(n)
newList = []
for a in range(len(pList)):
    nStr = str(pList[a])
    for i in range(len(numStr)):
        if nStr.count(numStr[i]) > 1:
            count = 0
            for j in range(i,len(numStr)):
                newStr = nStr.replace(numStr[i], numStr[j])
                if numbers.isPrime(newStr):
                    count = count + 1
            if count > 7:
                print(nStr)
                print("Time elapsed =", time.clock() - tic)

                sys.exit(1)

