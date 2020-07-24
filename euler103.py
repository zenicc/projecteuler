'''
Created on 24 July 2020
@author: Campbell



Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if for any two non-empty disjoint subsets, B and C, the following properties are true:

    S(B) ≠ S(C); that is, sums of subsets cannot be equal.
    If B contains more elements than C then S(B) > S(C).

If S(A) is minimised for a given n, we shall call it an optimum special sum set. The first five optimum special sum sets are given below.

n = 1: {1}
n = 2: {1, 2}
n = 3: {2, 3, 4}
n = 4: {3, 5, 6, 7}
n = 5: {6, 9, 11, 12, 13}

It seems that for a given optimum set, A = {a1, a2, ... , an}, the next optimum set is of the form B = {b, a1+b, a2+b, ... ,an+b}, where b is the "middle" element on the previous row.

By applying this "rule" we would expect the optimum set for n = 6 to be A = {11, 17, 20, 22, 23, 24}, with S(A) = 117. However, this is not the optimum set, as we have merely applied an algorithm to provide a near optimum set. The optimum set for n = 6 is A = {11, 18, 19, 20, 22, 25}, with S(A) = 115 and corresponding set string: 111819202225.

Given that A is an optimum special sum set for n = 7, find its set string.

NOTE: This problem is related to Problem 105 and Problem 106.

'''

import time, numpy, math, csv
from itertools import chain, combinations

def powerSet(iterable):
    # this returns all subsets of the passed set
    s = list(iterable)
    return list(chain.from_iterable(combinations(s, r) for r in range(1,len(s) + 1)))

def containsEqualSubsets(inSet):
    # this checks for whether a given set contains at least 2 subsets with the same sum

    checkList = [0]*(sum(inSet) + 1)
    llist = powerSet(inSet)
    for a in llist:
        checkList[sum(a)] += 1
        if checkList[sum(a)] > 1:
            return True

    return False

def longerSetRuleApplies(inSet):
    # this checks for whether any longer subset always has a greater sum than any shorter subset

    for n in range(2,int(math.ceil(len(inSet)/2))+1):
        #print(inSet[:n],inSet[-(n-1):])

        if not(sum(inSet[:n]) > sum(inSet[-(n-1):])):
            return False

    return True

def placeToNum(inList):
    # converts say [0, 0, 1, 0, 1, 1] to [3, 5, 6]
    aList = []
    for n in range(len(inList)):
        if inList[n] == 1:
            aList.append(n+1)
    return aList


def numToPlace(inList):
    # converts say [3, 5, 6] to [0, 0, 1, 0, 1, 1]
    aList = [0]*max(inList)
    for n in inList:
        aList[n-1] = 1
    return aList

def getNextNumber(a):
    b = numToPlace(a)
    #b.insert(0,0)
    #b.insert(0,1)
    b[0] = 1
    a = placeToNum(b)
    while not(longerSetRuleApplies(a)):
        b.insert(0,0)
        a = placeToNum(b)
    while containsEqualSubsets(a):
        pos = b.index(1)
        b.insert(pos+1, 0)
        a = placeToNum(b)
    return a

def reverseNumber(a):
    b = numToPlace(a)
    b.reverse()
    b.insert(0,0)
    return b

if __name__ == '__main__':
    # testing
    st = time.time()

    #a = [6, 9, 11, 12, 13]
    a = [11, 18, 19, 20, 22, 25]
    nextNo = getNextNumber(a)
    print(nextNo, sum(nextNo))

    revNo = reverseNumber(a)
    nextRevNo = getNextNumber(placeToNum(revNo))
    print(nextRevNo,sum(nextRevNo))
    '''
    b = [0,0,0,0,0,0,0,0,0,0,1, 0, 0, 0,0, 0, 1, 0, 0, 1, 0, 1, 1, 1]
    a = placeToNum(b)

    print(a)
    print(b)

    if longerSetRuleApplies(a):
        print(a, "meets longer set rule")
    else:
        print(a, "fails longer set rule **********")

    if containsEqualSubsets(a):
        print(a, " contains equal subsets **********")
    else:
        print(a, " is good")

    '''

    print("euler103 took %f seconds" % (time.time() - st))
