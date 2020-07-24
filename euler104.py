'''
Created on 24 July 2020
@author: Campbell



The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

It turns out that F541, which contains 113 digits, is the first Fibonacci number for which the last nine digits are 1-9
pandigital (contain all the digits 1 to 9, but not necessarily in order). And F2749, which contains 575 digits, is the first Fibonacci number for which the first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.

**********************************
Solution notes -

Straight forward brute force testing for front and back took ages - 20 minutes +. Guessed that the string operations on very large numbers was the problem.

Introduced a truncated version of the fibonacci series that just keeps the last 9 digits and test that every time.
If that is successful I then check for the first 9 digits on the full number thus removing nearly all the checks on the very large numbers. Ran in 7 secs..

'''

import time, numpy, math, csv, collections

if __name__ == '__main__':
    # testing
    st = time.time()

    digs = [1,2,3,4,5,6,7,8,9]

    F1 = 1
    F2 = 1
    shortF1 = 1
    shortF2 = 1
    k = 3
    notDone = True
    while notDone:
        Fk = F1 + F2
        F1 = F2
        F2 = Fk
        shortFk = (shortF1 + shortF2)%1000000000
        shortF1 = shortF2
        shortF2 = shortFk
        if Fk > 1000000000:
            Flst = [int(i) for i in str(shortFk)[-9:]]
            #print(k,Flst)
            if (collections.Counter(Flst) == collections.Counter(digs)):
                Fsta = [int(i) for i in str(Fk)[:9]]
                if (collections.Counter(Fsta) == collections.Counter(digs)):
                    print(k)
                    notDone = False
        k += 1



    print("euler104 took %f seconds" % (time.time() - st))
