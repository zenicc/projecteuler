'''
Created on 2015/06/02

@author: Campbell

Euler 61 - 

The cube, 41063625 (345**3), can be permuted to produce two other cubes: 56623104 (384**3) and 66430125 (405**3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.

'''
import time, numbers, sys, iccnumbers, collections, itertools

tic = time.clock()


#create all cubes
cubeList = list()
cubeList.append([])
cubeList.append([])

for n in range(10000):
        cubeNum = n**3
        
        cubeList[0].append(''.join(sorted(str(cubeNum))))
        cubeList[1].append(cubeNum)
'''
multList = [cube for cube,count in collections.Counter(cubeList[0]).items() if count>2]
print multList
'''
multList = collections.defaultdict(list)
for i,item in enumerate(cubeList[0]):
    multList[item].append(i)
multList = {k:v for k,v in multList.items() if len(v)>4}
print multList
print("Time elapsed =", time.clock() - tic)

sys.exit(1)

