'''
Created on 19 December 2018
@author: Campbell

The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:

28 = 2**2 + 2**3 + 2**4
33 = 3**2 + 2**3 + 2**4
49 = 5**2 + 2**3 + 2**4
47 = 2**2 + 3**3 + 2**4

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
'''

import time, csv
from getprimes import getPrimes

s = time.time()
count = 0
found = [0] * 50000000
primes = getPrimes(7072)
for a in primes:
    for b in primes:
        for c in primes:
            num = a**2 + b**3 + c**4
            if num >= 50000000:
                break
            else:
                 # print(num," = ", a, "**2 + ", b, "**3 + ",c, "**4 ",)
                 found[num] = 1

print(sum(found))

print("euler87 took %f seconds" % (time.time() - s))