'''
Created on 27 Dec 2011

@author: Campbell

Checks if the passed integer n is prime
'''
import time


def isPrime(n):
    "check if integer n is a prime"

    n = abs(int(n))
    limit = int((n ** 0.5)) + 2
    if n in [0, 1, 4, 6, 8, 9, 10]:
        return False

    if n < 11:
        return True

    if not n & 1:  # even
        return False

    if n % 3 == 0:
        return False

    for x in range(6, limit, 6):  # check for all 6k +- 1
        if (n % (x + 1) == 0):
            return False
        if (n % (x - 1) == 0):
            return False

    return True


def isPrime2(n):
    "check if integer n is a prime"

    n = abs(int(n))
    limit = int((n ** 0.5)) + 1
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, limit, 2):
        if n % x == 0:
            # print(x)
            return False
    return True


if __name__ == '__main__':
    # testing

    tic = time.clock()

    count1 = []
    count2 = []

    # num1 = 1111265717999981

    # print ("1 ", isPrime(1))
    # print ("2 ", isPrime(2))
    # print ("3 ", isPrime(3))
    # print ("8 ", isPrime(8))
    # print ("23 ", isPrime(23))
    # print ("999979 ", isPrime(999979))
    # print ("999985 ", isPrime(999985))
    for x in range(30):
        if isPrime(x):
            count1.append(x)

    print("Time elapsed =", time.clock() - tic)

    tic = time.clock()

    # print ("1 ", isPrime2(1))
    # print ("2 ", isPrime2(2))
    # print ("3 ", isPrime2(3))
    # print ("8 ", isPrime2(8))
    # print ("23 ", isPrime2(23))
    # print ("999979 ", isPrime2(999979))
    # print ("999985 ", isPrime2(999985))
    for x in range(30):
        if isPrime2(x):
            count2.append(x)

    print("count1 = ", len(count1))
    print("count2 = ", len(count2))
    print("count1 = ", count1)
    print("count2 = ", count2)

    print(set(count1) - set(count2))
    if isPrime(25):
        print("25 is prime")
    else:
        print("25 is compound")
    print("Time elapsed =", time.clock() - tic)
