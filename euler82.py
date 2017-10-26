'''
Created on 08 April 2017

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
        for x in range(1,len(inArray)):                
                for y in range(len(inArray)):
                        #print x,y,len(inArray),inArray[y][x]
                        if y > 0:
                                newPathTot = min(inArray[y][x-1],inArray[y-1][x])
                        else:
                                newPathTot = inArray[y][x-1]
                        rowNum = y+1
                        condTot = 0
                        while condTot < newPathTot and rowNum < len(inArray):
                                condTot += inArray[rowNum][x]
                                newPathTot = min(newPathTot, condTot + inArray[rowNum][x-1])
                                rowNum += 1
                        inArray[y][x] += newPathTot
                       # print inArray[y][x]
        return inArray

if __name__=='__main__':
    #testing
        s = time.time()
        T1 = list(csv.reader(open(r'./p082_matrix.txt')))
        T2 = [map(int, x) for x in T1]
        T3 = get_sum(T2)
        #print T3
        #print len(T3), len(T3[0])
        print min([i[-1] for i in T3])
        
        print("euler82 took %f seconds" % (time.time() - s))


    

