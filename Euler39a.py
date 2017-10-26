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

perCount = []


for a in range(1,aLim):
    for b in range(a+1, int((maxPer - a)/2)):
        c = (a**2 + b**2)**0.5
        if c == int(c): 
            perCount.append(int(a+b+c))
            #print (a, b, int(c), int(a + b + c))

print (max([(perCount.count(p), p) for p in set(perCount)]))
    
    
print("Time elapsed =", time.clock() - tic)

