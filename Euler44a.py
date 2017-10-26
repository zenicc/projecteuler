'''
Created on 2 Jan 2012

@author: Campbell

Euler 44 - find 2 pentagonal numbers where their sum and
difference are also pentagonal


'''
import time

def getPentagonalNos(limit):
    pentList = list()
    for n in range(1,limit):
        pentNo = n*(3*n-1)/2
        pentList.append(int(pentNo))
    return pentList

def isPent(n):
    x = (0.5 + ((0.25 + 6*n)**0.5))/3
    if x - int(x) == 0:
        return True
    else:
        return False

tic = time.clock()

numOfPents = 2500
penList = list(getPentagonalNos(numOfPents))
x = 0

for a in range(1,int(numOfPents/2)):
    for b in range(a+1,numOfPents - 1):
        x = penList[b]
        y = penList[a]
        if isPent(x-y) and isPent(x+y):
            print(x,y,x+y,x-y)

print("Time elapsed =", time.clock() - tic)

