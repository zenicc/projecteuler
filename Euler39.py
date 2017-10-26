'''
Created on 30 Dec 2011

@author: Campbell

Euler 39 - returns perimeter length of a right angled triangle that has the most
possible a,b,c combinations 
'''
import time

tic = time.clock()

maxPer = 1000 # maximum perimeter

aLim = int(maxPer/(2 + 2**0.5)) # maximum length of side a

perCount = list(range(maxPer))

for n in perCount:
    perCount[n] = 0


for a in range(1,aLim):
    for b in range(a+1, \
                   int(1 + ((maxPer**2) - (2 * maxPer * a))/(2 * (maxPer - a)))):
        c = (a**2 + b**2)**0.5
        if c == int(c): 
            perCount[int(a + b + c - 1)] += 1
            print (a, b, int(c), int(a + b + c))

perMaxCount = max(perCount)
perMax = perCount.index(perMaxCount)

print ("Perimeter with maximum possililities = ", perMax + 1)
print ("Number of possibilities = ", perMaxCount)
    
    
print("Time elapsed =", time.clock() - tic)

