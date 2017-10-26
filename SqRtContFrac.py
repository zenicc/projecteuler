# -*- coding: utf-8 -*-
'''
Created on 2015/09/14

@author: Campbell

Return approximations of the square root of a number as a continued fraction

'''
import time, numbers, sys, iccnumbers, collections, itertools

def getSquareRootParts(inNum):
    "returns square root expansion parts"
    
    mList = []
    nList = []
    bList = []
    
    L = int(inNum**0.5)

    mList.append(L)
    nList.append(1)
    bList.append(L)
    valuesFound = False
    for x in range(1,10): #number of approximations
            nList.append((inNum - bList[x-1]**2)/nList[x-1])
            mList.append(int((L + bList[x-1])/(nList[x])))
            bList.append(nList[x]* mList[x] - bList[x-1])
            a,b = contFracNumDen(mList)
            print mList
            print a,b, a*1.0/b

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
    
    getSquareRootParts(4)

    print("Time elapsed =", time.clock() - tic)

sys.exit(1)

