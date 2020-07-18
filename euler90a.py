'''
Created on 04 Nov 2019
@author: Campbell



Each of the six faces on a cube has a different digit (0 to 9) written on it; the same is done to a second cube. By placing the two cubes side-by-side in different positions we can form a variety of 2-digit numbers.

For example, the square number 64 could be formed:

In fact, by carefully choosing the digits on both cubes it is possible to display all of the square numbers below one-hundred: 01, 04, 09, 16, 25, 36, 49, 64, and 81.

For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on one cube and {1, 2, 3, 4, 8, 9} on the other cube.

However, for this problem we shall allow the 6 or 9 to be turned upside-down so that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows for all nine square numbers to be displayed; otherwise it would be impossible to obtain 09.

In determining a distinct arrangement we are interested in the digits on each cube, not the order.

{1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
{1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

But because we are allowing 6 and 9 to be reversed, the two distinct sets in the last example both represent the extended set {1, 2, 3, 4, 5, 6, 9} for the purpose of forming 2-digit numbers.

How many distinct arrangements of the two cubes allow for all of the square numbers to be displayed?


'''

import time, csv, math
from getprimes import getPrimes
from getFacts import getFacts

import numpy

s = time.time()
rowcnt = 9
cube = []
cubepair = [[]*2 for i in range(210*210)]
squares = [1,4,9,16,25,36,49,64,81]

#construct all cube possibilities
dierange = 10
count = 0
for d1 in range(dierange):
    for d2 in range(d1+1, dierange):
        for d3 in range(d2+1, dierange):
            for d4 in range(d3+1, dierange):
                for d5 in range(d4+1, dierange):
                    for d6 in range(d5+1, dierange):
                        cube.append([d1,d2,d3,d4,d5,d6])
                        count += 1

print(count)

# construct all cube pairings - note this includes pairings both ways
ind = 0
for n in cube:
    for m in cube:
        cubepair[ind].append(n)
        cubepair[ind].append(m)
        ind += 1

# construct all possible numbers from the 2 cubes
ccount = 0
for n in range(210*210):
    #print(cubepair[n])
    cubeprod = []
    for a in cubepair[n][0]:
        for b in cubepair[n][1]:
            cubeprod.append(10*a+b)
            cubeprod.append(10*b+a)
            if a == 6:
                cubeprod.append(90+b)
                cubeprod.append(10*b+9)
            if a == 9:
                cubeprod.append(60+b)
                cubeprod.append(10*b+6)
            if b == 6:
                cubeprod.append(10*a+9)
                cubeprod.append(90+a)
            if b == 9:
                cubeprod.append(10*a+6)
                cubeprod.append(60+a)

    #print(cubeprod)
    if all(x in cubeprod for x in squares):
        ccount += 1

print(ccount/2) # note we divide by 2 because the count includes duplicates as the cubes are included both ways



print("euler90 took %f seconds" % (time.time() - s))