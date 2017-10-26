'''
Created on 17 Dec 2012

@author: Campbell

Euler 55 - Find Lychrel numbers < 10,000. Lychrel is one where it doesn't
eventually give a palindromic number (within 50 iterations).
e.g. a non Lychrel number is 349
349 + 943 = 1292
1292 + 2921 = 4213
4213 + 3124 = 7337
'''
import time
from ispalindrome import ispalindrome

tic = time.clock()

count = 0

lList = []

#start loop of integers up to 10,000
for i in range(1,10000):
    num = i
    loop = 1
    Lychrel = True
    while Lychrel and loop <= 50:
        num = num + int(str(num)[::-1])
        if ispalindrome(str(num)):
           Lychrel = False
        else:
            loop = loop + 1

    if Lychrel:
        count = count + 1
        lList.append(i)
#end loop
print(count)
print(lList)

print("Time elapsed =", time.clock() - tic)
