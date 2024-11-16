"""
Created on 6 Jan 2023
@author: Campbell

Using a combination of grey square tiles and oblong tiles chosen from: red tiles (measuring two units), green tiles
(measuring three units), and blue tiles (measuring four units), it is possible to tile a row measuring five units in
length in exactly fifteen different ways.

png117.png

How many ways can a row measuring fifty units in length be tiled?



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
    neutral = 1
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

    print("euler117 took %f seconds" % (time.time() - s))
