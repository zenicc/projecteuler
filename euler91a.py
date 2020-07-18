'''
Created on 18 Nov 2019
@author: Campbell



The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates and are joined to the origin, O(0,0), to form ΔOPQ.

There are exactly fourteen triangles containing a right angle that can be formed when each co-ordinate lies between 0 and 2 inclusive; that is,
0 ≤ x1, y1, x2, y2 ≤ 2.

Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed?


'''

import time, csv, math
from getprimes import getPrimes
from getFacts import getFacts
from iccnumbers import gcd

import numpy

s = time.time()

rowcnt = 50


count = 0

xcheck = 1
ycheck = 4

count = 2*rowcnt*rowcnt #these are all the triangles with right angle along the axes
count += rowcnt*rowcnt #all triangles with right angle at origin
print("edge count ", count)
for ax in range(1,rowcnt+1): #treats each point not on an axis as a potential right angle
    for ay in range(1,rowcnt+1):
        g = gcd(ax, ay)
        xgrad = ay/g
        ygrad = ax/g
        cx = ax + xgrad
        cy = ay - ygrad
        if ax == xcheck and ay == ycheck:
            print(cx,cy)
        while cx <= rowcnt and cy >= 0:
            count += 1
            cx += xgrad
            cy -= ygrad
            if ax == xcheck and ay == ycheck:
                print(cx,cy)
        cx = ax - xgrad
        cy = ay + ygrad
        if ax == xcheck and ay == ycheck:
            print(cx,cy)
        while cx >= 0 and cy <= rowcnt:
            count += 1
            cx -= xgrad
            cy += ygrad
            if ax == xcheck and ay == ycheck:
                print(cx,cy)


print(count)


print("euler91 took %f seconds" % (time.time() - s))