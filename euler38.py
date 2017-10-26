'''
Created on 28 Dec 2011

@author: Campbell

euler 38
'''
import time

tic = time.clock()


def isPandig(n):
    
    candStr = ""
    i = 1
    while len(candStr) < 9:
        candStr += str(n*i)
        i += 1
    if len(candStr) > 9 or candStr.find('0') > 0:
        return 0
    elif len(set(candStr)) == 9:
        return int(candStr)
    else:
        return 0
    
highNum = 0

for n in range(9000, 10000):
    candidateNum = isPandig(n)
    if candidateNum > highNum:
        highNum = candidateNum

print (highNum)
print("Time elapsed =", time.clock() - tic)

