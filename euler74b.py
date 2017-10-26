# -*- coding: utf-8 -*-
'''
Created on 2016/01/01

@author: Campbell

The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

'''
import time, sys, numbers, math

def getFactSum(n):
# Return the sum of the factorials of each digit of n
# e.g. if n = 24, then 2! + 4! = 26 is returned
                
    tot = 0
    while n > 9:
        rem = n%(10*(n/10))
        n = n/10
        tot += math.factorial(rem)
    return tot + math.factorial(n)
            

if __name__=='__main__':
    #testing ********************************************* test individual returns for getFactSum *************************
    s = time.time()
    switcher = {
        145: 0,
        169: 2,
        871: 1,
        872: 1,
    }
    cnt = 0
    x = 363601
    num = x
    print(getFactSum(num))
    while num not in(145,169,871,872):
        cnt += 1
        if num in (1,2):
            break
        if cnt > 60:
            break
        num = getFactSum(num) 
        #print("Factorial sum of {0} = {1}".format(x, num))
    cnt = cnt + switcher.get(num, 999)
    print ("Chain for {0} = {1}".format(x, cnt))
    print("Euler 74 took %f seconds" % (time.time() - s))

sys.exit(1)
