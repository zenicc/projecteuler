"""
Created on 11 Nov 2024
@author: Campbell

Using all of the digits 1 through 9 and concatenating them freely to form decimal integers, different sets can be formed.
Interestingly with the set {2,5,47,89,631}, all of the elements belonging to it are prime.

How many distinct sets containing each of the digits one through nine exactly once contain only prime elements?

"""

import iccnumbers, itertools, time

"""
def getPrimesNoDup(n):
    # as a starting point attempt to get all primes without repeated digits. Works but far too slow.
    numsIn = iccnumbers.getPrimes(n)
    numsOut = []
    # remove primes with repeated digits
    for number in numsIn:
        if len(set(str(number))) == len(str(number)):
    # print(number)
            numsOut.append(number)
    return numsOut
"""
def getAllNumPerms():
    # get all permutations of digits

    numsOut = list(itertools.permutations([1, 2, 3, 4,5, 6, 7, 8, 9]))

    return numsOut

def getAllPrimeCombs(numList):
    """ return all combinations of all prime numbers for the list of numbers passed
    Partition a list into all possible sublists. eg [1,2,3,4] will give [1,2,3,4], [1,2,34], [1,23,4], [1, 234],
    [12,3,4], [12,34], [123,4], [1234].

    This uses a number such as 101 to show there is a gap where there is a 1 but none where 0. So 101 would return [1,23,4]

    Then return those sublists where all numbers are prime."""

    n = len(numList)
    partList = []

    primeCombs = []

    for partitionIndex in range(2 ** (n - 1)):
        partition = []
        subset = ""
        for position in range(n):

            subset = subset + str(numList[position])

            if 1 << position & partitionIndex or position == n - 1:
                partition.append(int(subset))
                subset = ""
        partList.append(partition)
        # print(partition)

    # print(partList)

    # test whether the partitions are prime
    for part in partList:
        prime = True
        for n in part:
            if not iccnumbers.isPrime(n):
                prime = False
                break
        if prime:
            primeCombs.append(part.sort())

    return primeCombs

if __name__ == '__main__':
    # testing

    s = time.time()

    count = 0
    combList = getAllNumPerms()
    #print(combList)

    for cList in combList:
        primeList = getAllPrimeCombs(cList)
        #print(primeList)
        count += len(primeList)

    print(count)
    print("euler118 took %f seconds" % (time.time() - s))
