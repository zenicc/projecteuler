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
loop through all lists eliminating those that cannot be in a sequence
        
'''

for n in range(4):

        triListSh = []
        triListSh.append([])
        triListSh.append([])
        triListSh.append([])

        for a in range(len(triList[0])):
                if triList[2][a] not in (squareList[1] + pentList[1] + hexList[1] + hepList[1] + octList[1]) \
                or triList[1][a] not in (squareList[2] + pentList[2] + hexList[2] + hepList[2] + octList[2]):
                        print "tri deleted ", triList[0][a]
                else:
                        triListSh[0].append(triList[0][a])
                        triListSh[1].append(triList[1][a])
                        triListSh[2].append(triList[2][a])

        squareListSh = []
        squareListSh.append([])
        squareListSh.append([])
        squareListSh.append([])



        for a in range(len(squareList[0])):
                if squareList[2][a] not in (triListSh[1] + pentList[1] + hexList[1] + hepList[1] + octList[1]) \
                or squareList[1][a] not in (triListSh[2] + pentList[2] + hexList[2] + hepList[2] + octList[2]):
                        print "square deleted ", squareList[0][a]
                else:
                        squareListSh[0].append(squareList[0][a])
                        squareListSh[1].append(squareList[1][a])
                        squareListSh[2].append(squareList[2][a])

        pentListSh = []
        pentListSh.append([])
        pentListSh.append([])
        pentListSh.append([])

        for a in range(len(pentList[0])):
                if pentList[2][a] not in (triListSh[1] + squareListSh[1] + hexList[1] + hepList[1] + octList[1]) \
                or pentList[1][a] not in (triListSh[2] + squareListSh[2] + hexList[2] + hepList[2] + octList[2]):
                        print "pent deleted ", squareList[0][a]
                else:
                        pentListSh[0].append(pentList[0][a])
                        pentListSh[1].append(pentList[1][a])
                        pentListSh[2].append(pentList[2][a])

        hexListSh = []
        hexListSh.append([])
        hexListSh.append([])
        hexListSh.append([])

        for a in range(len(hexList[0])):
                if hexList[2][a] not in (triListSh[1] + squareListSh[1] + pentListSh[1] + hepList[1] + octList[1]) \
                or hexList[1][a] not in (triListSh[2] + squareListSh[2] + pentListSh[2] + hepList[2] + octList[2]):
                        print "hex deleted ", squareList[0][a]
                else:
                        hexListSh[0].append(hexList[0][a])
                        hexListSh[1].append(hexList[1][a])
                        hexListSh[2].append(hexList[2][a])

        hepListSh = []
        hepListSh.append([])
        hepListSh.append([])
        hepListSh.append([])

        for a in range(len(hepList[0])):
                if hepList[2][a] not in (triListSh[1] + squareListSh[1] + pentListSh[1] + hexListSh[1] + octList[1]) \
                or hepList[1][a] not in (triListSh[2] + squareListSh[2] + pentListSh[2] + hexListSh[2] + octList[2]):
                        print "hep deleted ", hepList[0][a]
                else:
                        hepListSh[0].append(hepList[0][a])
                        hepListSh[1].append(hepList[1][a])
                        hepListSh[2].append(hepList[2][a])

        octListSh = []
        octListSh.append([])
        octListSh.append([])
        octListSh.append([])

        for a in range(len(octList[0])):
                if octList[2][a] not in (triListSh[1] + squareListSh[1] + pentListSh[1] + hexListSh[1] + hepListSh[1]) \
                or octList[1][a] not in (triListSh[2] + squareListSh[2] + pentListSh[2] + hexListSh[2] + hepListSh[2]):
                        print "oct deleted ", octList[0][a]
                else:
                        octListSh[0].append(octList[0][a])
                        octListSh[1].append(octList[1][a])
                        octListSh[2].append(octList[2][a])

        del octList
        del hepList
        del hexList
        del pentList
        del squareList
        del triList

        octList = octListSh
        hepList = hepListSh
        hexList = hexListSh
        pentList = pentListSh
        squareList = squareListSh
        triList = triListSh

        del octListSh
        del hepListSh
        del hexListSh
        del pentListSh
        del squareListSh
        del triListSh



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
					
print("Time elapsed =", time.clock() - tic)

sys.exit(1)

