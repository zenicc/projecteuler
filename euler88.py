'''
Created on 13 June 2019
@author: Campbell



A natural number, N, that can be written as the sum and product of a given set of at least two natural numbers, {a1, a2, ... , ak} is called a product-sum number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.

For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.

For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number. The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.

k=2: 4 = 2 × 2 = 2 + 2
k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6

Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30; note that 8 is only counted once in the sum.

In fact, as the complete set of minimal product-sum numbers for 2≤k≤12 is {4, 6, 8, 12, 15, 16}, the sum is 61.

What is the sum of all the minimal product-sum numbers for 2≤k≤12000?

'''

import time, csv
from getprimes import getPrimes
from getFacts import getFacts
'''
This will find all possible candidate sets for each possible sum, check on whether each candidate is the first set found 
for the set length and keep a record if it is.
'''
s = time.time()
count = 0
k = 12000
minList = [0] * (k + 1)
checklim = k + 400 #this is to make sure all ks are found as the min product-sums are greater than k
primes = getPrimes(checklim)
for a in range(4, checklim):
    if a not in primes:
        factSet = getFacts(a)
        #print(a, factSet)
        for set in factSet:
            leng = int(len(set) + a - sum(set))
            if leng <= k and minList[leng] == 0:
                minList[leng] = a

for ind in range(2, k):
    print(ind, " - ", minList[ind])

nonduplist = list(dict.fromkeys(minList) )
print(sum(nonduplist))



print("euler88 took %f seconds" % (time.time() - s))