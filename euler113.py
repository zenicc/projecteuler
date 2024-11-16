"""
Created on 17 Nov 2021
@author: Campbell


Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

As n increases, the proportion of bouncy numbers below n increases such that there are only 12951 numbers below one-million that are not bouncy and only 277032 non-bouncy numbers below 10**10.

How many numbers below a googol (10**100) are not bouncy?


"""

import time

import iccnumbers, numpy

def numBouncy(n):
    # returns true if n is bouncy, false if not
    up = False
    down = False

    numList = [int(x) for x in str(n)]

    for a in range(1, len(numList)):
        if numList[a] > numList[a-1]:
            up = True
        if numList[a] < numList[a-1]:
            down = True
        if up and down:
            return True

    return False

if __name__ == '__main__':
    # testing
    st = time.time()

    bouncyCount = 0
    nonBouncyCount = 0
    bouncy = ["not bouncy", "bouncy"]

    count = 10**10



    for n in range(1, count):
        if numBouncy(n):
            bouncyCount += 1
        else:
            nonBouncyCount += 1

    print(bouncyCount, nonBouncyCount)

    print("euler113 took %f seconds" % (time.time() - st))
