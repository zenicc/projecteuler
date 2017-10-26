import time, sys
from iccnumbers import isPrime,getPrimes

tic = time.clock()

limit = 10000

primes = getPrimes(limit)

s1 = dict()
s2 = set()
s3 = set()
s4 = set()

for p in primes:
    s1[p] = set()
    for s in s1:
        if isPrime(int(str(p) + str(s))) and isPrime(int(str(s) + str(p))):
            s1[s].add(p)
            s1[p].add(s)
            s2.add((s, p))
            
            
    for s in s2:
        if p in s1[s[0]] and p in s1[s[1]]: s3.add((s[0], s[1], p))
    for s in s3:
        if p in s1[s[0]] and p in s1[s[1]] and p in s1[s[2]]: s4.add((s[0], s[1], s[2], p))
    for s in s4:
        if p in s1[s[0]] and p in s1[s[1]] and p in s1[s[2]] and p in s1[s[3]]: print p, s
#print s1
print "time elapsed = ",  time.clock() - tic
sys.exit(1)
