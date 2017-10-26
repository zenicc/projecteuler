'''
Created on 28 Dec 2011

@author: Campbell

returns list of all permutations of inList items as strings
'''
import time
from itertools import permutations

tic = time.clock()


def is_concat_pandig(n):
    
    c = ""
    i = 1
    while len(c) < 9:
        c += str(n*i)
        i += 1
    if len(c) > 9 or c.find('0') > 0:
        return 0
    elif len(set(c)) == 9:
        return int(c)
    else:
        return 0
    
hi = 0

for n in range(1, 10**4):
    t = is_concat_pandig(n)
    if t and t > hi:
        hi = t

print (hi)
print("Time elapsed =", time.clock() - tic)

