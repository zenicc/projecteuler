'''
Created on 2 Jan 2012

@author: Campbell


'''

import time, math, itertools

def isPrime(n):
    "check if integer n is a prime"

    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def isPrime2(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def isPermutation(num1, num2):
    "check if num1 is a permutation of num2"
    if sorted(str(num1)) == sorted(str(num2)):
        return True
    else:
        return False

def getNumPerm(n):
    "return a set of all permutaions of the given number ie for 123 return {123,132,213,231,312,321}"
    l = itertools.permutations(str(n))
    return [int(''.join(x)) for x in l if int(''.join(x)) >= n]

def getPrimeFactors(n):
    if n < 2:
        return []
    prime_factors = []
    for p in getPrimes(int(n**0.5) + 1):
        if p*p > n: break
        while n % p == 0:
            if p not in prime_factors:
                prime_factors.append(p)
            n //= p
    if n > 1:
        prime_factors.append(n)
    return prime_factors

def getPrimeFactorsList(n, primeList):
    if n < 2:
        return []
    prime_factors = []
    for p in primeList:
        if p*p > n: break
        while n % p == 0:
            if p not in prime_factors:
                prime_factors.append(p)
            n //= p
    if n > 1:
        prime_factors.append(n)
    return prime_factors

def getPrimeFactorsZ(n, primeList):
    "return all prime factors for the number passed" 
    if n < 2:
        return []
    if n == 2:
        return [2]
    if n == 3:
        return [3]
    factorList = []
    Factored = False
    a = 0
    while not Factored:
        if n%primeList[a] == 0:
            if primeList[a] not in factorList:
                factorList.append(primeList[a])
            rem = n/primeList[a]
            if isPrime(rem):
                if rem not in factorList:
                    factorList.append(rem)
                Factored = True
            if rem == 1:
                Factored = True
            else:
                print n, a, primeList, factorList
                n = n/a
        else:
            a += 1
    return factorList
           
def getPrimeFactorsY(n):
    "return all prime factors for the number passed"
    factorList = []
    primeList = getPrimes(n/2 + 1)
    for a in primeList:
        if n%a == 0:
            factorList.append(a)
    return factorList

def getPrimeFactorsX(n):
    #quite slow
    "return all prime factors for the number passed" 
    factorList = []
    for a in range(2, int(n/2)+1):
        if n%a == 0 and isPrime(a):
            factorList.append(a)
    return factorList
           

def getPentagonalNos(limit):
    pentList = list()
    for n in range(1,limit):
        pentNo = n*(3*n-1)/2
        pentList.append(int(pentNo))
    return pentList

def getGenPentagonalNos(limit):
    pentList = list()
    for n in range(1,limit):
        pentNo = n*(3*n-1)/2
        pentList.append(int(pentNo))
        pentNo = -n*(3*-n-1)/2
        pentList.append(int(pentNo))
    return pentList

def isTri(n):
    x = -0.5 + ((0.25 + 2*n)**0.5)
    if x - int(x) == 0:
        return True
    else:
        return False

def isPent(n):
    x = (0.5 + ((0.25 + 6*n)**0.5))/3
    if x - int(x) == 0:
        return True
    else:
        return False

def isHex(n):
    x = (1 + ((1 + 8*n)**0.5))/4
    if x - int(x) == 0:
        return True
    else:
        return False


def getPrimes(n):
    "return a list of all primes up to n"
 
    if n==2: return [2]
    elif n<2: return []
    lim = int(n**.5) + 1
    primeList = list(range(n+1))
    primeList[1] = 0
    for a in range(2, lim):
        if primeList[a]:
            lim2 = int(n/a) + 1
            for b in range(2, lim2):
                c = a*b
                try:
                    primeList[c] = 0
                except ValueError:
                    pass 
    return [x for x in primeList if x]

   
def comb(n, r):
    "return nCr"
    if 0 <= r <= n:
        return math.factorial(n)/(math.factorial(r)*math.factorial(n - r))
    else:
        return 0

def sumDigits(n):
   r = 0
   while n:
       r = r + n % 10
       n = n / 10
   return r

def gcd(a,b):

    if a == b:
        return a
    if a == 0:
        return b
    if b == 0:
        return a

    shift=0
   
    while (a|b)&1 ==0:
        # while a and b are both even divide by 2 and keep score of divisions
        a>>=1
        b>>=1
        shift+=1
   
    while a&1==0:
        # while a is even, keep dividing by 2
        a>>=1
           
    while b>0:
        # while either a or b are not 0, keep subtracting one from the other
        while b&1==0:
            # while b is even, keep dividing by 2
            b>>=1
        if a>b: 
            t=a
            a=b
            b=t
       
        b=b-a
       
    return a<<shift

def farey( n, asc=True ):
    "Return the nth Farey sequence, either ascending or descending."
    fareyL = []
    if asc: 
        a, b, c, d = 0, 1,  1 , n     # (*)
    else:
        a, b, c, d = 1, 1, n-1, n     # (*)
    fareyL.append(str(a) + "/" + str(b))
    while (asc and c <= n) or (not asc and a > 0):
        k = int((n + b)/d)
        a, b, c, d = c, d, k*c - a, k*d - b
        fareyL.append(str(a) + "/" + str(b))

    return fareyL

def getSqRoot(n, p):
    "square root of n to p decimal places."
    r = 1.5
    for i in range(8):
        r = 0.5*(r + n/r)
        print r
    

    return r

if __name__=='__main__':
    #testing
    s = time.time()
    print(getSqRoot(5.0,100))
        
    print("Took %f seconds" % (time.time() - s))

    
