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
import time, numbers

if __name__=='__main__':
    #testing
        s = time.time()
        n=60000
        p = [0]*n
        polyList = numbers.getGenPentagonalNos(int(n**0.5))
        #print("getting pent numbers took %f seconds" % (time.time() - s))
        p[0] = 1
        for i in range(1,n):
                total = 0
                for j in range(i):
                        k = polyList[j]
                        #print(i,k)
                        if p[i-k] == 0:
                                break
                        if j%4 < 2:
                                sign = 1
                        else:
                                sign = -1
                        total += sign*p[i - k]
                p[i] = total%1000000
                if p[i] == 0:
                        print(i,p[i])
                        break
        print(p[i])
        print("euler78 took %f seconds" % (time.time() - s))


    

