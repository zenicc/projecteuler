'''
Created on 2 Jan 2012

@author: Campbell

Euler 44 - find 2 pentagonal numbers where their sum and
difference are also pentagonal


'''
import time

tic = time.clock()

s=set([1,5])
x=5
y=1
dx=7
dy=4
while True:
    if (x-y)%2==0:
        if int((x-y)/2) in s:
            if int((x+y)/2) in s:
                print(y)
                break
    y+=dy
    dy+=3
    if y==x:
        x+=dx
        dx+=3
        y,dy=1,4
        s.add(x)

print("Time elapsed =", time.clock() - tic)

