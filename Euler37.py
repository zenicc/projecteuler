'''
Created on 27 Dec 2011

@author: Campbell

Euler 37 - returns total of all 11 numbers which are prime
and truncatable from both left and right'''
import time
from isprime import isprime

tic = time.clock()

def allPrime(n):

    if isprime(int(n)):
        prime = True
        for l in range(1,len(str(n))):
            if isprime(int(n[:-l])):
                if isprime(int(n[l:])):
                    True
                else:
                    prime = False
                    break
            else:
                 prime = False
                 break
    else:
        prime = False

    return prime

if __name__=='__main__':
    #testing

    tic = time.clock()
    print (sum(num for num in range(11,1000000,2) if allPrime(str(num))))
    #for num in range(11,1000000,2):
        #if allPrime(str(num)):
            #print (num, "all prime")
    #num = 3797    
    #print (num, "all prime", allPrime(str(num)))
    print("Time elapsed =", time.clock() - tic)

