import time, numbers, sys, iccnumbers
tic = time.clock()
def catnums(n1,n2):
	return int(str(n1)+str(n2))
#@memoized
def catable(n1,n2):
	return iccnumbers.isPrime(catnums(n1,n2)) and iccnumbers.isPrime(catnums(n2,n1))
def p60():
	maxp,targetlen=10000,5
	ps=iccnumbers.getPrimes(maxp)
	def check(cset=[]):
		if len(cset)==targetlen: return cset
		base = len(cset) and cset[-1]+1 or 0
		for i in xrange(base,len(ps)):
			if reduce(lambda x,y: x and y, [catable(ps[i],ps[j]) for j in cset], True):
				cset.append(i)
				if check(cset): return cset
				else: cset.pop()
		return None
	result=check()
	if result: return [ps[i] for i in result]
	else: return None
print p60()
print "time elapsed = ",  time.clock() - tic
sys.exit(1)
