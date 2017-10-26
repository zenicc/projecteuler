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

tic = time.clock()

numOfPents = 2500
penList = list(getPentagonalNos(numOfPents))
#penList = [2,4,6,8,10,12,14,16,18,20]
maxPent = max(penList)

for a in range(1,int(numOfPents/2)):
    for b in range(a+1,numOfPents - 1):
        if penList[b] + penList[a] > maxPent:
            break
        else:
            if ((penList[b] + penList[a]) in penList) and  \
            ((penList[b] - penList[a]) in penList):
                print (penList[a],penList[b],penList[b] + penList[a],
                       penList[b] - penList[a])
    
    
print("Time elapsed =", time.clock() - tic)

