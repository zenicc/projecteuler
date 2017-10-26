'''
Created on 21 June 2016

@author: Campbell


'''
from math import sqrt
import time
def P(n):
    if n<0: return 0
    if PN[n]: return PN[n]
    total = 0
    for k in range(1,int(sqrt(n))+1):
        pn1, pn2 = P(n - k*(3*k+1)/2), P(n - k*(3*k-1)/2)
        total += pn1+pn2 if k%2 else -pn1-pn2
    PN[n] = total % 1000000
    return PN[n]


s = time.time()
PN = [0]*100000
PN[0] = 1
i = 1
while P(i): i+=1
print i, PN[i]
print("Took %f seconds" % (time.time() - s))
