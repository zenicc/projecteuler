'''
Created on 04 Nov 2019
@author: Campbell



Each of the six faces on a cube has a different digit (0 to 9) written on it; the same is done to a second cube. By placing the two cubes side-by-side in different positions we can form a variety of 2-digit numbers.

For example, the square number 64 could be formed:

In fact, by carefully choosing the digits on both cubes it is possible to display all of the square numbers below one-hundred: 01, 04, 09, 16, 25, 36, 49, 64, and 81.

For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on one cube and {1, 2, 3, 4, 8, 9} on the other cube.

However, for this problem we shall allow the 6 or 9 to be turned upside-down so that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows for all nine square numbers to be displayed; otherwise it would be impossible to obtain 09.

In determining a distinct arrangement we are interested in the digits on each cube, not the order.

{1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
{1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

But because we are allowing 6 and 9 to be reversed, the two distinct sets in the last example both represent the extended set {1, 2, 3, 4, 5, 6, 9} for the purpose of forming 2-digit numbers.

How many distinct arrangements of the two cubes allow for all of the square numbers to be displayed?

THE APPROACH BELOW - GENERATE POSSIBILITIES FROM THE SQUARES - DOESN'T SEEM TO WORK. NOT ALL POSSIBILITIES ARE FOUND.

'''

import time, csv
from getprimes import getPrimes
from getFacts import getFacts

import numpy

s = time.time()
rowcnt = 9
square = numpy.zeros((rowcnt, 2))

for n in range(rowcnt):
    square[n][0] = ((n + 1) ** 2) // 10
    square[n][1] = ((n + 1) ** 2) % 10
print(square)

cpcnt = 2 ** (rowcnt - 1)
cube = numpy.zeros((cpcnt, rowcnt, 2))
outcube = numpy.zeros((cpcnt, 2, rowcnt))
outcube2 = [[[]*9 for i in range(2)] for j in range(cpcnt)]

for n in range(cpcnt):
    cube[n][0][1] = 1

for row in range(1, rowcnt):
    outloopmax = 2 ** (row - 1)
    inloopmax = int(cpcnt / (outloopmax * 2))
    for outloop in range(1, outloopmax + 1):
        for inloop in range(1, inloopmax + 1):
            cubepair = 2 * inloopmax * (outloop - 1) + inloop - 1
            cube[cubepair][row][0] = square[row][0]
            cube[cubepair][row][1] = square[row][1]
        for inloop in range(inloopmax + 1, 2 * inloopmax + 1):
            cubepair = 2 * inloopmax * (outloop - 1) + inloop - 1
            cube[cubepair][row][0] = square[row][1]
            cube[cubepair][row][1] = square[row][0]

for n in range(cpcnt):
    outcube[n] = numpy.transpose(cube[n])

for n in range(cpcnt):
    for m in range(2):
        outcube2[n][m].append(list(set(outcube[n][m])))

for n in range(cpcnt):
    for m in range(2):
        print(outcube2[n][m])
        if outcube2[n][m] == [[1, 2, 3, 4, 8, 9]]:
            print('****************************************************************')

    print()

print("euler90 took %f seconds" % (time.time() - s))