'''
Created on 10 July 2016

@author: Campbell


In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right,
by only moving to the right and down, is 131, 201, 96, 342, 746, 422, 121, 37, 331 is equal to 2427.

131,673,234,103,18
201,96, 342,965,150
630,803,746,422,111
537,699,497,121,956
805,732,524,37, 331

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."),
a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.

'''


import time, csv
from decimal import *

def get_sum(inArray):
        for y in range(1,len(inArray)):
                inArray[y][0] += inArray[y-1][0]
                inArray[0][y] += inArray[0][y-1]
                
        for y in range(1,len(inArray)):
                
                inArray[y][y] += min(inArray[y-1][y],inArray[y][y-1])
                for y1 in range(y+1, len(inArray)):
                        inArray[y1][y] += min(inArray[y1-1][y],inArray[y1][y-1])
                        inArray[y][y1] += min(inArray[y-1][y1],inArray[y][y1-1])
        return inArray

if __name__=='__main__':
    #testing
        s = time.time()
        T1 = list(csv.reader(open(r'./p081_matrix.txt')))
        T2 = [map(int, x) for x in T1]
        T3 = get_sum(T2)
        #print T3
        print len(T3), len(T3[0])
        print T3[len(T3)-1][len(T3[0])-1]
        
        print("euler81 took %f seconds" % (time.time() - s))


    

