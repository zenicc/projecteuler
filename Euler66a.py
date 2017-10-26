# -*- coding: utf-8 -*-
'''
Created on 2015/06/07

@author: Campbell

Euler 66 - 

For the equation x**2 - D * y**2 = 1 (Pell's Equation)
Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.

'''
import time, numbers, sys, iccnumbers, collections, itertools

def getSquareRootParts(inNum):
    "returns square root expansion parts that satisfy equation"
    
    mList = []
    nList = []
    bList = []
    
    L = int(inNum**0.5)

    mList.append(L)
    nList.append(1)
    bList.append(L)
    valuesFound = False
    for x in range(1,1000): #abitrary max value - satisfying value of x will be reached well within this
            nList.append((inNum - bList[x-1]**2)/nList[x-1])
            mList.append(int((L + bList[x-1])/(nList[x])))
            bList.append(nList[x]* mList[x] - bList[x-1])
            a,b = contFracNumDen(mList)
            if a**2 - inNum*(b**2) == 1:
                    return a,b

def contFracNumDen(listt):
    
    if len(listt) == 2: 
    	a = listt[0]
    	b = listt[1]
    	return (a * b) + 1, b
    else:
    	a = listt[0]
    	den, num = contFracNumDen(listt[1:])#switch num and den to get inversion
    	return (a * den) + num, den 

if __name__=='__main__':
    #testing

    tic = time.clock()
    maxX = 0
    maxD = 0
    for D in range(3):
        if D**0.5 != int(D**0.5): # will not work for exact squares
            x,y = getSquareRootParts(D)
            print D,x,y
            if x > maxX:
                maxX = x
                maxD = D
    print(maxD, maxX)

    print("Time elapsed =", time.clock() - tic)

sys.exit(1)

