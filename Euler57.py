'''
Created on 18 Dec 2012

@author: Campbell

Euler 57 - In the first one-thousand expansions of the
fraction series for 2**.5, how many fractions contain a
numerator with more digits than denominator?
'''
import time
from ispalindrome import ispalindrome

tic = time.clock()

count = 0
n = 3
d = 2
for i in range(1,1000):
    nextn = n + 2*d
    nextd = n + d
    n = nextn
    d = nextd
    #print(n,d)
    if len(str(n)) > len(str(d)):
        count = count + 1        
    
print(count)

print("Time elapsed =", time.clock() - tic)
