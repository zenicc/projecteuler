'''
Created on 16 April 2020
@author: Campbell

The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form
2**6972593 − 1; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2**p − 1,
have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433 × 2**7830457 + 1.

Find the last ten digits of this prime number.


Solution basis -

Find the repeat pattern for the last 10 digits of the powers of 2 then find where 7830457 fits into the repeating pattern.

The pattern starts at 2**m and repeats every 4 * 5**(m-1) powers where m is the number of digits you want. So in this
case we have the start as 2**10 = 1024 and the repeat length as 4 * 5**9 = 7812500
'''

import time, numpy


st = time.time()

digNeeded = 10

repStart = 2**digNeeded
repLen = 4*5**(digNeeded - 1)
n = 7830457

pow2 = (2**(digNeeded + (n - digNeeded)%repLen))

print(pow2)

print((28433*pow2+1)%(10**10))

print("euler97 took %f seconds" % (time.time() - st))
