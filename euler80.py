'''
Created on 23 June 2016

@author: Campbell


It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots
is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.

'''


import time
from decimal import *

if __name__=='__main__':
    #testing
        s = time.time()
        getcontext().prec = 105
        tot = 0
        for i in range(100):
                n = Decimal(i).sqrt()
                if not n == int(n):
                        n = int(n*(10**99))
                        tot += sum(int(ch) for ch in str(n) if ch.isdigit())
        print("total = %f" % tot)
        print("euler78 took %f seconds" % (time.time() - s))


    

