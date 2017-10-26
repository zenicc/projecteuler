'''
Created on 2014/08/26

@author: Campbell

Euler 61 - The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting properties.

    The set is cyclic, in that the last two digits of each number is the first two digits of the next number (including the last number with the first).
    Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and pentagonal (P5,44=2882), is represented by a different number in the set.
    This is the only set of 4-digit numbers with this property.

Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal,
and octagonal, is represented by a different number in the set.
'''
import time, numbers, sys, iccnumbers, collections, itertools

tic = time.clock()



#create all 4 digit pentagonal numbers

pentList = list()
pentList.append([])
pentList.append([])
pentList.append([])

for n in range(2000):
        pentNum = n*(3*n-1)/2
        if pentNum > 9999:
                break
        if pentNum > 999:
                pentList[0].append(pentNum)
                pentList[1].append(str(pentNum)[0:2])
                pentList[2].append(str(pentNum)[2:4])

#create all 4 digit square numbers

squareList = list()
squareList.append([])
squareList.append([])
squareList.append([])

for n in range(2000):
        squareNum = n*n
        if squareNum > 9999:
                break
        if squareNum > 999:
                squareList[0].append(squareNum)
                squareList[1].append(str(squareNum)[0:2])
                squareList[2].append(str(squareNum)[2:4])

#create all 4 digit triangle numbers

triList = []
triList.append([])
triList.append([])
triList.append([])

for n in range(2000):
        triNum = n*(n + 1)/2
        if triNum > 9999:
                break
        if triNum > 999:
                triList[0].append(triNum)
                triList[1].append(str(triNum)[0:2])
                triList[2].append(str(triNum)[2:4])


'''
loop through all lists 
        
'''

origList = [triList, squareList, pentList]

Found = False

loopCount = 0
for x in list(itertools.permutations([0,1,2])):
        print "loop count = ", loopCount
        listZero = origList[x[0]]
        listOne = origList[x[1]]
        listTwo = origList[x[2]]
       # print len(triList[0]), len(listOne[0]), len(listTwo[0])
        for a in range(len(listZero[0])):
            for b in range(len(listOne[0])):
               if listZero[2][a] == listOne[1][b]:
                   for c in range(len(listTwo[0])):
                       #print a,b,c
                       if listOne[2][b] == listTwo[1][c] and listTwo[2][c] == listZero[1][a]:
                           Found = True
                           print (listZero[0][a], " = ", listOne[0][b], " = ",
                                  listTwo[0][c])
                           break
        #if Found:
        #        break
        loopCount += 1
        print "new loop count = ", loopCount

        



'''
print octList
print "**********************************"
print hepList
print "**********************************"
print hexList
print "**********************************"
print pentList
print "**********************************"
print squareList
print "**********************************"
print triList
'''					
print("Time elapsed =", time.clock() - tic)

sys.exit(1)

