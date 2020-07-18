'''
Created on 20 Dec 2019
@author: Campbell


It is easily proved that no equilateral triangle exists with integral length sides and integral area. However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).
312530794631114590 - wrong answer!!!
'''

import time, csv, math

import numpy

st = time.time()
perim = 0
triangles = []
limit = 1000000
for n in range(2,int(limit/3 + 1)):
    bigger = ((n+1)*(3.0*n*n - 2 * n - 1)**(.5))/4
    smaller = ((n-1)*(3.0*n*n + 2 * n - 1)**(.5))/4
    if bigger == int(bigger):
        perim += 2*n+n+1
        triangles.append([n,n+1])
        #print(n,n+1,perim,bigger)
    if smaller == int(smaller):
        perim += 2*n+n-1
        triangles.append([n,n-1])
        #print(n,n-1,perim,smaller)

print(triangles)
print(perim)
print("euler94 took %f seconds" % (time.time() - st))