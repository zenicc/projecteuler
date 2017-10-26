'''
Created on 2015/06/17

@author: Campbell

Euler 67 - Using the numbers 1 to 10, and depending on arrangements,
it is possible to form 16- and 17-digit strings. What is the maximum 16-digit string for a "magic" 5-gon ring?'''
import time, numbers, sys, iccnumbers, collections, itertools

tic = time.clock()


for x in list(itertools.permutations([1,2,3,4,5,6,7,8,9,10])):
        if (x[0] + x[1] + x[2] == x[3] + x[2] + x[4] and
            x[0] + x[1] + x[2] == x[5] + x[4] + x[6] and
            x[0] + x[1] + x[2] == x[7] + x[6] + x[8] and
            x[0] + x[1] + x[2] == x[9] + x[8] + x[1] and
            x[0] < x[3] and
            x[0] < x[5] and
            x[0] < x[7] and
            x[0] < x[9]):
                print x[0],x[1],x[2],'-', x[3],x[2],x[4],'-',x[5],x[4],x[6],'-',x[7],x[6],x[8],'-',x[9],x[8],x[1]
				
print("Time elapsed =", time.clock() - tic)

sys.exit(1)

