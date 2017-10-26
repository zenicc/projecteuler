# -*- coding: utf-8 -*-
'''
Created on 2015/11/09

@author: Campbell



Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?



'''
#import time, numbers, sys, iccnumbers, collections, itertools
import time
start = time.time()
lim = 8
x = 1 / 3.0
smallest = 1
for i in range(1,lim + 1):
    for j in range(1,i):
        if j / float(i) > x:
            if j / float(i) < smallest:
                smallest = j / float(i)
                c_d_pair = (j,i)
            break
c , d = c_d_pair
a = 1
b = 3
count = 1
while True:
    print a,b,c,d
    a , b , c , d = c , d , ((lim + b) / d) * c - a , ((lim + b) / d) * d - b
    if d == 2 and c == 1:
         ,print a,b,c,d
        print count
        print time.time() - start
        break
    count += 1
