'''
Created on 2014/04/28

@author: Campbell

Euler 60 - The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
'''
import time, numbers, sys, iccnumbers, collections

tic = time.clock()


#create a dict where each row is a list of reversible combined primes indexed by the prime
n = 10000
pList = iccnumbers.getPrimes(n)
qList = list(pList)
ppDict = collections.defaultdict(list)
for p in pList:
	ppDict[p].append(p)
	qList.remove(p)

	for q in qList:
		if (iccnumbers.isPrime(int(str(p)+str(q))) and 
		iccnumbers.isPrime(int(str(q)+str(p)))):
			ppDict[p].append(q)
			ppDict[q].append(p)
print pList[-1]
#extract into a list only those rows with candidate length
ppList = [v for k,v in ppDict.iteritems() if len(v)>4]
print 'ppList length = ', len(ppList)

#get those items which intersect the required number of rows	
for a in range(len(ppList) - 4):
	for b in range(a+1,len(ppList) - 3):
		for c in range(b+1,len(ppList) - 2):
			itemSha = list(set(ppList[a]) & set(ppList[b]))
			if len(itemSha) < 5:
				break
			for d in range(c+1,len(ppList) - 1):
				itemShb = list(set(itemSha) & set(ppList[c]))
				if len(itemShb) < 5:
					break
				for e in range(d+1,len(ppList)):
					itemShc = list(set(itemShb) & set(ppList[d]))
					if len(itemShc) < 5:
						break
					itemSh = list(set(itemShc) & set(ppList[e]))
				#itemSh = [1]
					if len(itemSh) > 4:
						print itemSh, sum(itemSh)
					
print("Time elapsed =", time.clock() - tic)

sys.exit(1)

