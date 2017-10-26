'''
Created on 2014/04/28

@author: Campbell

Euler 60 - The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

This just gathers pairs of primes where this is true.
'''
import time, numbers, sys, iccnumbers

tic = time.clock()

'''''''''''''''''''''''''''''
Get list of primes
'''''''''''''''''''''''''''''

n = 10000
pList = iccnumbers.getPrimes(n)
print "Highest prime = ", pList[-1]
lenPList = len(pList)
print "Number of primes = ", lenPList
	
print "Got primes - time elapsed = ",  time.clock() - tic


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Get list of prime pairs where their concatenation is also a prime
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

tic = time.clock()
ppList2 = []
for m in range(0,lenPList-1):
        for n in range(m,lenPList):
                if (iccnumbers.isPrime(int(str(pList[m]) + str(pList[n]))) and 
                iccnumbers.isPrime(int(str(pList[n]) + str(pList[m])))): 
                        ppList2.append([pList[m], pList[n]])
#print ppList                        
print "pairs time elapsed = ",  time.clock() - tic

'''''''''''''''''''''''''''''''''
Get chains of paired primes
'''''''''''''''''''''''''''''''''

tic = time.clock()

for p in ppList2:
        if p[1] in 

'''''''''''''''''''''''''''''''''

for p in range(len(ppList)):
        tempList = [x for x in ppList if x[0] == ppList[p][1]]#all the pairs in ppList where 1st part = 2nd part of the current pair 
        for q in range(len(tempList)):
                if [ppList[p][0],tempList[q][1]] in ppList:
                        tempList2 = [x for x in ppList if x[0] == tempList[q][1]]#all the pairs in ppList where 1st part = 2nd part of the tempList
                        for r in range(len(tempList2)):
                                if ([ppList[p][0],tempList2[r][1]] in ppList and
                                     [tempList[q][0],tempList2[r][1]] in ppList):
                                        tempList3 = [x for x in ppList if x[0] == tempList2[r][1]]#all the pairs in ppList where 1st part = 2nd part of the tempList1
                                        for s in range(len(tempList3)):
                                                if ([ppList[p][0],tempList3[s][1]] in ppList and
                                                     [tempList[q][0],tempList3[s][1]] in ppList and
                                                     [tempList2[r][0],tempList3[s][1]] in ppList):
                                                        print [ppList[p][0],ppList[p][1],tempList[q][1],tempList2[r][1],tempList3[s][1]]

'''                     
print "triples time elapsed = ",  time.clock() - tic
sys.exit(1)

