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


def make_tuples(depth, start, finish):
    if depth == 0:
        yield ()
    else:
        if finish > start:
            up = 1
        else:
            up = -1
        # for x in range(start, finish, up):
        # for t in make_tuples(depth - 1, x + up, finish):
        for x in range(start, finish, up):
            for t in make_tuples(depth - 1, x, finish):
                yield (x,) + t



if __name__ == '__main__':
    # testing
    st = time.time()

    digitNo = 100
    countup = 0
    countdown = 0
    eqcount = 0
    for n in range(1, digitNo + 1):
        print(n, time.time() - st)
        for (i1) in make_tuples(n, 1, 10):
            # do stuff with i1, i2, i3
            # print(i1)
            countup += 1
        for (i1) in make_tuples(n, 9, -1):
            # do stuff with i1, i2, i3
            # print(i1)
            countdown += 1
        eqcount += 10

    print(countup, countdown, eqcount,  countup + countdown - eqcount)

    print("euler113a took %f seconds" % (time.time() - st))
