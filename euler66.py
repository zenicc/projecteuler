# -*- coding: utf-8 -*-
'''
Created on 2015/06/04

@author: Campbell

Euler 66 - 

x**2 – Dy**2 = 1

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.
'''
#import time, numbers, sys, iccnumbers, collections, itertools
import time, sys, numbers

s = time.time()
maxX = 1
maxY = 1
maxD = 1
for D in range(61,62):
        if D**0.5 != int(D**0.5):
                y = 1
                found = False
                while not found:
                        #y = ((x**2 - 1.0)/D)**0.5
                        x = (1 + D*(y**2))**0.5
                        #print(x,y,D)
                        if (int(x))**2 - D*(y**2) == 1 and y != 0:
                                found = True
                                #print(x,y,D)
                                if x > maxX:
                                        maxX = x
                                        maxY = y
                                        maxD = D
                        else:
                                y += 1
print("Max x =", maxX)
print("Max y =", maxY)
print("Max D =", maxD)
print("Euler 66 took %f seconds" % (time.time() - s))

sys.exit(1)

