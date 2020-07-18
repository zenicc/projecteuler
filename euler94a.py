'''
Created on 20 Dec 2019
@author: Campbell


It is easily proved that no equilateral triangle exists with integral length sides and integral area. However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).

This solution uses Heronian triangle theory
'''

import time, csv, math

import numpy

st = time.time()
perim = 0
triangles = []
limit = 1000000000
for v in range(1,int((limit/3 - 1)**.5)):
    for u in range(v+1,int((limit/3 - v*v)**.5)):
        if (v+u)%2 == 1:
            a = u*u+v*v
            b = u*u+v*v
            c = 2*(u*u - v*v)
            d = 4*u*v
            if abs(a-c) == 1:
                triangles.append([a,c,a+b+c])
                perim += a+b+c
            if abs(a-d) == 1:
                triangles.append([a,d,a+b+d])
                perim += a+b+d

print(triangles)
print(perim)
print("euler94 took %f seconds" % (time.time() - st))