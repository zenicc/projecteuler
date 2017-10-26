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

octList = list()
octList.append([])
octList.append([])
octList.append([])

for n in range(2000):
        octNum = n*(3*n-2)
        if octNum > 9999:
                break
        if octNum > 999:
                octList[0].append(octNum)
                octList[1].append(str(octNum)[0:2])
                octList[2].append(str(octNum)[2:4])
                
#create all 4 digit heptagonal numbers

hepList = list()
hepList.append([])
hepList.append([])
hepList.append([])

for n in range(2000):
        hepNum = n*(5*n-3)/2
        if hepNum > 9999:
                break
        if hepNum > 999:
                hepList[0].append(hepNum)
                hepList[1].append(str(hepNum)[0:2])
                hepList[2].append(str(hepNum)[2:4])

#create all 4 digit hexagonal numbers

hexList = list()
hexList.append([])
hexList.append([])
hexList.append([])

for n in range(2000):
        hexNum = n*(2*n-1)
        if hexNum > 9999:
                break
        if hexNum > 999:
                hexList[0].append(hexNum)
                hexList[1].append(str(hexNum)[0:2])
                hexList[2].append(str(hexNum)[2:4])

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
listOne = squareList
listTwo = pentList
listThree = hexList
listFour = hepList
listFive = octList


origList = [triList, squareList, pentList, hexList, hepList, octList]

Found = False

loopCount = 0
for x in list(itertools.permutations([0,1,2,3,4,5])):
        #print "loop count = ", loopCount
        listZero = origList[x[0]]
        listOne = origList[x[1]]
        listTwo = origList[x[2]]
        listThree = origList[x[3]]
        listFour = origList[x[4]]
        listFive = origList[x[5]]
        for a in range(len(listZero[0])):
            for b in range(len(listOne[0])):
               if listZero[2][a] == listOne[1][b]:
                   for c in range(len(listTwo[0])):
                       if listOne[2][b] == listTwo[1][c]:
                           for d in range(len(listThree[0])):
                               if listTwo[2][c] == listThree[1][d]:
                                   for e in range(len(listFour[0])):
                                       if listThree[2][d] == listFour[1][e]:
                                           for f in range(len(listFive[0])):
                                               if listFour[2][e] == listFive[1][f] and listFive[2][f] == triList[1][a]:
                                                   Found = True
                                                   print (listZero[0][a], " = ", listOne[0][b], " = ",
                                                          listTwo[0][c], " = ", listThree[0][d], " = ", 
                                                          listFour[0][e], " = ", listFive[0][f])
                                                   print "sum = ", listZero[0][a] + listOne[0][b] + listTwo[0][c] + listThree[0][d] + listFour[0][e] + listFive[0][f]
                                                   break
        if Found:
                break
                                               
        loopCount += 1
        #print "new loop count = ", loopCount

        



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

