'''
Created on 18 Nov 2019
@author: Campbell



The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates and are joined to the origin, O(0,0), to form ΔOPQ.

There are exactly fourteen triangles containing a right angle that can be formed when each co-ordinate lies between 0 and 2 inclusive; that is,
0 ≤ x1, y1, x2, y2 ≤ 2.

Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed?


'''

import time, csv, math
from getprimes import getPrimes
from getFacts import getFacts

import numpy

s = time.time()
rowcnt = 3

count = 0
tri1 = []
tri2 = []
for ax in range(rowcnt+1):
    for ay in range(rowcnt+1):
        for bx in range(rowcnt+1):
            for by in range(rowcnt+1):
                oa = ax**2 + ay**2
                ob = bx**2 + by**2
                ab = (ax - bx)**2 + (ay - by)**2
                if ab > oa and ab > ob:
                    if ab == oa + ob:
                        count += 1
                        tri1.append([ax,ay,bx,by])
                        tri2.append([oa,ob,ab])
                else:
                    if oa > ab and oa > ob:
                        if oa == ab + ob:
                            count += 1
                            tri1.append([ax,ay,bx,by])
                            tri2.append([oa,ob,ab])
                    else:
                        if ob > ab and ob > oa:
                            if ob == ab + oa:
                                count += 1
                                tri1.append([ax,ay,bx,by])
                                tri2.append([oa,ob,ab])

#print(tri1)
print(count/2)


print("euler91 took %f seconds" % (time.time() - s))