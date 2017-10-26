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
import time, numbers, sys, iccnumbers, collections

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
listOne = []
listOne.append([])
listOne.append([])
listOne.append([])

listOne = triList

listTwo = []
listTwo.append([])
listTwo.append([])
listTwo.append([])

listTwo = squareSList

Found = False

for a in range(len(triList[0])):
    for b in range(len(squareList[0])):
       if triList[2][a] == squareList[1][b]:
           for c in range(len(pentList[0])):
               if squareList[2][b] == pentList[1][c]:
                   for d in range(len(hexList[0])):
                       if pentList[2][c] == hexList[1][d]:
                           for e in range(len(hepList[0])):
                               if hexList[2][d] == hepList[1][e]:
                                   for f in range(len(octList[0])):
                                       if hepList[2][e] == octList[1][f] and octList[2][f] == triList[1][a]:
                                           found = True
                                           print (triList[0][a], " = ", squareList[0][b], " = ",
                                                  pentList[0][c], " = ", hexList[0][d], " = ", 
                                                  hepList[0][e], " = ", octList[0][f])
for a in range(len(triList[0])):
    for b in range(len(squareList[0])):
       if triList[2][a] == squareList[1][b]:
           for c in range(len(pentList[0])):
               if squareList[2][b] == pentList[1][c]:
                   for d in range(len(hexList[0])):
                       if pentList[2][c] == hexList[1][d]:
                           for e in range(len(octList[0])):
                               if hexList[2][d] == octList[1][e]:
                                   for f in range(len(hepList[0])):
                                       if octList[2][e] == hepList[1][f] and hepList[2][f] == triList[1][a]:
                                           found = True
                                           print (triList[0][a], " = ", squareList[0][b], " = ",
                                                  pentList[0][c], " = ", hexList[0][d], " = ", 
                                                  octList[0][e], " = ", hepList[0][f])

        



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

