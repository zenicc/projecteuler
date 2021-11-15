'''
Created on 14 June 2019

@author: Campbell


'''
import time, iccnumbers, timeit


def getFacts(n):
    "return all factorisations of n"

    factList = []
    for a in range(2, int(n ** 0.5) + 1):
        if n % a == 0:
            c = n / a
            factList.append([a, c])
            if c > a and not iccnumbers.isPrime(c):
                subsets = getFacts(c)
                for b in subsets:
                    if a <= min(b):
                        factList.append([a] + b)
    return factList


if __name__ == '__main__':
    # testing
    s = time.time()
    a = []
    n = 27719
    max = 0
    a = getFacts(n)
    print(a)
    print("First took %f seconds" % (time.time() - s))
    s = time.time()
