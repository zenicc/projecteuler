'''
Created on 12 April 2017

@author: Campbell


In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by moving left, right, up, and down, is indicated in bold red and is equal to 2297.

131,673,234,103,18
201,96, 342,965,150
630,803,746,422,111
537,699,497,121,956
805,732,524,37, 331

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by moving left, right, up, and down.
'''
#*****************************************************************************************************************************
#COPIED FROM PROJECT EULER FORUM - THIS DOES NOT SEEM TO WORK!!!!!!!!!
#******************************************************************************************************************************


import time, csv
from decimal import *


s = time.time()
T1 = list(csv.reader(open(r'./p083_matrix_test.txt')))
#T1 = list(csv.reader(open(r'./p083_matrix.txt')))
gg2 = [map(int, x) for x in T1]

WIDTH = len(gg2)
HEIGHT = len(gg2)
a = [[0 for col in range(WIDTH)] for row in range(HEIGHT)]
perm = [[False for col in range(WIDTH)] for row in range(HEIGHT)]

a[0][0] = gg2[0][0]
perm[0][0] = True
a[0][1] = gg2[0][0] + gg2[0][1]
a[1][0] = gg2[0][0] + gg2[1][0]

cnt = 0
while(cnt != WIDTH*HEIGHT):       
	miny = 0
	minx=0
	minval=99999999
	for y in range(HEIGHT):
                
		for x in range(WIDTH):
		
			if(a[y][x] < minval and not(perm[y][x])):
			
				minval = a[y][x]
				miny = y
				minx = x
			
		
                
	y = miny
	x = minx
	perm[y][x] = True
	cnt+=1

	
	if(y != 0):
		if(a[y][x] + gg2[y-1][x] < a[y-1][x]):
			a[y-1][x] = a[y][x] + gg2[y-1][x]
	
	if(y != HEIGHT-1):
		if(a[y][x] + gg2[y+1][x] < a[y+1][x]):
			a[y+1][x] = a[y][x] + gg2[y+1][x]
	
	if(x != 0):
		if(a[y][x] + gg2[y][x-1] < a[y][x-1]):
			a[y][x-1] = a[y][x] + gg2[y][x-1]
	
	if(x != WIDTH-1):
		if(a[y][x] + gg2[y][x+1] < a[y][x+1]):
			a[y][x+1] = a[y][x] + gg2[y][x+1]

print a
print("euler83 took %f seconds" % (time.time() - s))
