'''
Created on 21 Dec 2011

@author: Campbell

'''
import time
from math import factorial

tic = time.clock()
facts = [factorial(x) for x in range(10)]

for a in range(9):
    facta = 0
    if a > 0:
        facta = facts[a]
    for b in range(9):
        factb = 0
        if a > 0 or b > 0:
            factb = facts[b]
        for c in range(9):
            factc = 0
            if a > 0 or b > 0 or c > 0:
                factc = facts[c]
            for d in range(9):
                factd = 0
                if a > 0 or b > 0 or c > 0 or d > 0:
                    factd = facts[d]
                for e in range(9):
                    facte = 0
                    if a > 0 or b > 0 or c > 0 or d > 0 or e > 0:
                        facte = facts[e]
                    for f in range(9):
                        factf = 0
                        if a > 0 or b > 0 or c > 0 or d > 0 or e > 0 or f > 0:
                            factf = facts[f]
                        fact = facta + factb + factc + factd + facte + factf
                        num = 100000*a + 10000*b + 1000*c + 100*d + 10*e + f
                        if fact == num:
                            print(num)
    
print("Time elapsed =", time.clock() - tic)
