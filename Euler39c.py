'''
Created on 30 Dec 2011

@author: Campbell

Euler 39 - returns perimeter length of a right angled triangle that has the most
possible a,b,c combinations 
'''
import time

tic = time.clock()

# create list of primitive pythagorean triples perimiter lengths
primitivePerimList = []
for v in range(1,23):
    for u in range(1,v+1):
        if ((v+u) % 2 == 1):
            primitivePerimList.append(2*(v**2) + (2*v*u))

# create list of all perimeter lengths obtainable from primitive list
allPerimList = []
for primPerim in primitivePerimList:
    for allPerim in range(primPerim, 1000):
        if allPerim % primPerim == 0:
            allPerimList.append(allPerim)


print (max([(allPerimList.count(p), p) for p in set(allPerimList)]))
    
    
print("Time elapsed =", time.clock() - tic)

