'''
Created on 23 Dec 2019
@author: Campbell



The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:

12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding one million.

'''

import time, csv, math

import numpy

st = time.time()

limit = 1000000
factorSumList = [0] * (limit + 1)
maxLen = 0
minAmi = 0

factorSumList[0] = 1
factorSumList[1] = 1
for v in range(1,int(limit/2)+1):
    for u in range(2*v,limit+1,v):
        factorSumList[u] += v

for i in range(1,limit+1):
    if factorSumList[i] > 1:
        chainList = [i]
        n = factorSumList[i]
        while not(n == i) and n > 1 and not(n > limit):
            chainList.append(n)
            n = factorSumList[n]
            if not(n==i) and n in chainList:
                n = 1
        if n == i and len(chainList) > maxLen:
            maxLen = len(chainList)
            minAmi = min(chainList)
            print(chainList)


print(maxLen, minAmi)

print("euler95 took %f seconds" % (time.time() - st))