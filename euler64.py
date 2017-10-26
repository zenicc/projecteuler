'''
Created on 2015/06/03

@author: Campbell

Euler 64 - 

How many odd period square roots are there <= 10000 - see question for more info!!

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
    repeatFound = False
    for x in range(1,1000):
            nList.append((inNum - bList[x-1]**2)/nList[x-1])
            mList.append(int((L + bList[x-1])/(nList[x])))
            bList.append(nList[x]* mList[x] - bList[x-1])
            if mList[x] == 2*L:
                    repeatFound = True
                    break
    if not repeatFound:
            print "No repeat on", inNum
    return mList


if __name__=='__main__':
    #testing

    tic = time.clock()

    oddCount = 0
    for num in range(3):
            if num**0.5 != int(num**0.5):
                    sqRtBreakdown = getSquareRootParts(num)
                    print num, ' => ', sqRtBreakdown
                    if len(sqRtBreakdown) %2 == 0:
                            oddCount += 1

    print 'Odd count =', oddCount

    print("Time elapsed =", time.clock() - tic)

sys.exit(1)

