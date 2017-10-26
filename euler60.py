'''
Created on 2014/04/28

@author: Campbell

Euler 60 - The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
'''
import time, numbers, sys, iccnumbers

tic = time.clock()


n = 20000000
pList = iccnumbers.getPrimes(n)
print "Highest prime = ", pList[-1]
lenPList = len(pList)

		
print "Got primes - time elapsed = ",  time.clock() - tic 
a = 3
b = 7
c = 109
d = 673
achar = str(a)
bchar = str(b)
cchar = str(c)
dchar = str(d)
found = False 
ind = 0
while not found and ind < lenPList:
        if (iccnumbers.isPrime(int(achar + str(pList[ind]))) and 
                iccnumbers.isPrime(int(bchar + str(pList[ind]))) and 
                iccnumbers.isPrime(int(cchar + str(pList[ind]))) and 
                iccnumbers.isPrime(int(dchar + str(pList[ind]))) and 
                iccnumbers.isPrime(int(str(pList[ind]) + achar)) and 
                iccnumbers.isPrime(int(str(pList[ind]) + bchar)) and 
                iccnumbers.isPrime(int(str(pList[ind]) + cchar)) and 
                iccnumbers.isPrime(int(str(pList[ind]) + dchar))): 
                print pList[ind]
                found = True
        else:
                ind = ind + 1

if not found: print "Not Found"		
print "Time elapsed = ", time.clock() - tic 

sys.exit(1)

