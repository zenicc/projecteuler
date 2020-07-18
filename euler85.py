'''
Created on 19 December 2018

@author: Campbell

By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:

Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.


'''

import time, csv

s = time.time()
for c in range(1,2829):
    for r in range(c,2829):
        rec_count = ((c*(c+1))/2)*((r*(r+1))/2)
        if abs(2000000 - rec_count) < 100:
            print(c,r,c*r,rec_count)

print("euler85 took %f seconds" % (time.time() - s))