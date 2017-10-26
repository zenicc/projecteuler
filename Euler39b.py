'''
Created on 30 Dec 2011

@author: Campbell

Euler 39 - returns perimeter length of a right angled triangle that has the most
possible a,b,c combinations 
'''
import time

tic = time.clock()

pythTripleList = []

# create list of pythagorean triples
for v in range(1,51):
    for u in range(1,v+1):
        if ((v+u) % 2 == 1):
            a = v**2-u**2
            b = 2*v*u
            c = v**2+u**2
            if a**2 + b**2 == c**2:
                pythTripleList.append( (a,b,c) )

vals = {}
for a,b,c in pythTripleList:
    perLen = a+b+c
    for p in range(perLen,1000):
        if p % perLen == 0:
            if p not in vals:
                vals[p] = 1
            else:
                vals[p] += 1

max = 0
i = 0
for k,v in vals.items():
    if v > max:
        max = v
        i = k

print (i,max)
    
    
print("Time elapsed =", time.clock() - tic)

