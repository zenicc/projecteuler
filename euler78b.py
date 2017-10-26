'''
Created on 21 June 2016

@author: Campbell

Let p(n) represent the number of different ways in which n coins can be separated into piles. For example,
five coins can be separated into piles in exactly seven different ways, so p(5)=7.
OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O

Find the least value of n for which p(n) is divisible by one million.

'''

# Note to myself - this is much quicker than euler78 original -
# the thing that makes the biggest difference is the way the inner loop works.
# All methods use the recursive formula over pentagonal numbers
# p[n] = p[n-1] + p[n-2] - p[n-5] - p[n-7] + p[n-12] etc.
import time, numbers

if __name__=='__main__':
    #testing
        s = time.time()
        polyList = numbers.getGenPentagonalNos(250)
        print polyList
        sign = [1,1,-1,-1]
        p = [1]
        i = 0
        while p[i] > 0:
                i += 1
                total = 0
                j = 0
                while polyList[j] <= i:
                        total += sign[j%4]*p[i - polyList[j]]
                        j += 1
                p.append(total%1000000)
        print(i)
        print("euler78 took %f seconds" % (time.time() - s))


    

