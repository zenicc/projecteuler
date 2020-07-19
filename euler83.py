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


import time, csv
from decimal import *

def get_heuristics(inArray):

        outArray=[[0 for i in range(len(inArray))] for j in range(len(inArray))]

        minValue = max
        cols = len(inArray)
        rows= len(inArray)
        for x in range(rows):
                for y in range(cols):
                        if inArray[x][y] < minValue:
                                minValue = inArray[x][y]
        #print minValue
        
        for x in range(rows):
                for y in range(cols):
                        outArray[rows-x-1][rows-y-1] = minValue*(x+y)

        
        return outArray

def get_min_boundary(boundaryArray):
        
        minValue = max
        cols = len(boundaryArray)
        rows= len(boundaryArray)
        minSquare = [0,0]
        for x in range(rows):
                for y in range(cols):
                        if boundaryArray[x][y] < minValue:
                                minValue = boundaryArray[x][y]
                                minSquare = [x,y]
        
        return minSquare

def update_boundaryArray(candSquare, boundaryArray, resultArray, baseArray, heurArray):

        x = candSquare[0]
        y = candSquare[1]

        if (x>0 and resultArray[x-1][y] == 0 and boundaryArray[x-1][y] == max): 
                boundaryArray[x-1][y] = resultArray[x][y] + baseArray[x-1][y] + heurArray[x-1][y]
        if (y>0 and resultArray[x][y-1] == 0 and boundaryArray[x][y-1] == max): 
                boundaryArray[x][y-1] = resultArray[x][y] + baseArray[x][y-1] + heurArray[x][y-1]
        if (x+1<len(boundaryArray) and resultArray[x+1][y] == 0 and boundaryArray[x+1][y] == max): 
                boundaryArray[x+1][y] = resultArray[x][y] + baseArray[x+1][y] + heurArray[x+1][y]
        if (y+1<len(boundaryArray) and resultArray[x][y+1] == 0 and boundaryArray[x][y+1] == max): 
                boundaryArray[x][y+1] = resultArray[x][y] + baseArray[x][y+1] + heurArray[x][y+1]

        boundaryArray[x][y] = max
            
        return boundaryArray
                    

if __name__=='__main__':
    #testing
        s = time.time()
        #T1 = list(csv.reader(open(r'./p083_matrix_test.txt')))
        T1 = list(csv.reader(open(r'./p083_matrix.txt')))
        baseArray = [map(int, x) for x in T1]
        heurArray = get_heuristics(baseArray)
        boundaryArray = [[max for col in range(len(baseArray))] for row in range(len(baseArray))]
        resultArray = [[0 for col in range(len(baseArray))] for row in range(len(baseArray))]

        candSquare = [0,0]
        targetSquare = [len(baseArray)-1, len(baseArray)-1]

        resultArray[candSquare[0]][candSquare[1]] = baseArray[candSquare[0]][candSquare[1]]

        while candSquare != targetSquare:
                boundaryArray = update_boundaryArray(candSquare, boundaryArray, resultArray, baseArray, heurArray)
                nextSquare = get_min_boundary(boundaryArray)
                resultArray[nextSquare[0]][nextSquare[1]] = boundaryArray[nextSquare[0]][nextSquare[1]] - heurArray[nextSquare[0]][nextSquare[1]]
                candSquare = nextSquare
        
        
        print(resultArray[len(baseArray)-1][len(baseArray)-1])
        
        print("euler83 took %f seconds" % (time.time() - s))


    

