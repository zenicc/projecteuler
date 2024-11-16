"""
Created on 17 Nov 2021
@author: Campbell




Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.

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
    numCount = 0
    bouncy = ["not bouncy", "bouncy"]

    percLim = .99

    while True:
        numCount += 1
        if numBouncy(numCount):
            bouncyCount += 1
        #print(bouncyCount, numCount, bouncyCount/numCount, bouncy[numBouncy(numCount)])
        if bouncyCount/numCount >= percLim:
            break

    print(bouncyCount, numCount, bouncyCount/numCount)

    print("euler112 took %f seconds" % (time.time() - st))
