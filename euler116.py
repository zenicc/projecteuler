"""
Created on 31 Jan 2022
@author: Campbell



A row of five grey square tiles is to have a number of its tiles replaced with coloured oblong tiles chosen from red (length two), green (length three), or blue (length four).

If red tiles are chosen there are exactly seven ways this can be done.
png116_1.png

If green tiles are chosen there are three ways.
png116_2.png

And if blue tiles are chosen there are two ways.
png116_3.png

Assuming that colours cannot be mixed there are 7 + 3 + 2 = 12 ways of replacing the grey tiles in a row measuring five units in length.

How many different ways can the grey tiles in a row measuring fifty units in length be replaced if colours cannot be mixed and at least one coloured tile must be used?

NOTE: This is related to Problem 117.



"""

import iccnumbers, time


def getBcombos(gridlen, blen):

    g = int(gridlen/blen)
    tot = 0

    for n in range(1, g+1):
        tot += iccnumbers.comb(n+(gridlen-(n*blen)), n)

    return tot


if __name__ == '__main__':

    #testing

    s = time.time()
    red = 2
    green = 3
    blue = 4

    gridlen = 50

    redc = getBcombos(gridlen, red)
    greenc = getBcombos(gridlen, green)
    bluec = getBcombos(gridlen, blue)

    print(redc)
    print(greenc)
    print(bluec)
    print('gridlen ' + str(gridlen) + ' total = ' + str(redc + greenc + bluec))

    print("euler116 took %f seconds" % (time.time() - s))
