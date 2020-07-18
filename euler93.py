'''
Created on 03 Dec 2019
@author: Campbell



By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and making use of the four arithmetic operations (+, −, *, /) and brackets/parentheses, it is possible to form different positive integer targets.

For example,

8 = (4 * (1 + 3)) / 2
14 = 4 * (3 + 1 / 2)
19 = 4 * (2 + 3) − 1
36 = 3 * 4 * (2 + 1)

Note that concatenations of the digits, like 12 + 34, are not allowed.

Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different target numbers of which 36 is the maximum, and each of the numbers 1 to 28 can be obtained before encountering the first non-expressible number.

Find the set of four distinct digits, a < b < c < d, for which the longest set of consecutive positive integers, 1 to n, can be obtained, giving your answer as a string: abcd.

'''

import time, csv, math
from getprimes import getPrimes
from getFacts import getFacts
from iccnumbers import gcd

import numpy

st = time.time()
sym = ['+', '-', '*', '/']
res = [[0 for x in range(6*7*8*9+1)] for y in range(6*7*8*9+1)]
maxFound = 0

row = 1
for a in range(1,10):
    for b in range(a+1,10):
        for c in range(b+1,10):
            for d in range(c+1,10):
                numset = [a,b,c,d]
                res[row][0] = numset
                for p in numset:
                    for q in list(set(numset) - set([p])):
                        for r in list(set(numset) - set([p,q])):
                            for s in list(set(numset) - set([p,q,r])):
                                for s1 in sym:
                                    for s2 in sym:
                                        for s3 in sym:
                                            candcalc = str(p) + s1 + str(q) + s2 + str(r) + s3 + str(s)
                                            answ = eval(candcalc)
                                            if answ == int(answ) and answ > 0:
                                                res[row][int(answ)] = 1
                                            if s1 in ["+", "-"]:
                                                candcalc = "(" + str(p) + s1 + str(q) + ")" + s2 + str(r) + s3 + str(s)
                                                answ = eval(candcalc)
                                                if answ == int(answ) and answ > 0:
                                                    res[row][int(answ)] = 1
                                                if s3 in ["+", "-"]:
                                                    candcalc = "(" + str(p) + s1 + str(q) + ")" + s2 + "(" + str(r) + s3 + str(s) + ")"
                                                    answ = eval(candcalc)
                                                    if answ == int(answ) and answ > 0:
                                                        res[row][int(answ)] = 1
                                            if s2 in ["+", "-"]:
                                                candcalc = str(p) + s1 + "(" + str(q) + s2 + str(r) + ")" + s3 + str(s)
                                                answ = eval(candcalc)
                                                if answ == int(answ) and answ > 0:
                                                    res[row][int(answ)] = 1
                                            if s3 in ["+", "-"]:
                                                candcalc = str(p) + s1 + str(q) + s2 + "(" + str(r) + s3 + str(s) + ")"
                                                answ = eval(candcalc)
                                                if answ == int(answ) and answ > 0:
                                                    res[row][int(answ)] = 1
                                                if not(s1 == "/"):
                                                    candcalc = str(p) + s1 + "(" + "(" + str(q) + s2 + str(r) + ")" + s3 + str(s) + ")"
                                                    answ = eval(candcalc)
                                                    if answ == int(answ) and answ > 0:
                                                        res[row][int(answ)] = 1

                index = res[row].index(0)
                if index > maxFound:
                    maxFound = index
                    maxRow = res[row][0]
                if d == 4:
                    print(res[row])
                    print(res[row][0], index - 1)

                row += 1

print(maxRow, maxFound)
print("euler93 took %f seconds" % (time.time() - st))