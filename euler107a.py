'''
Created on 28 July 2020
@author: Campbell



The following undirected network consists of seven vertices and twelve edges with a total weight of 243.

The same network can be represented by the matrix below.
    	A	B	C	D	E	F	G
A	    -	16	12	21	-	-	-
B	    16	-	-	17	20	-	-
C	    12	-	-	28	-	31	-
D	    21	17	28	-	18	19	23
E	    -	20	-	18	-	-	11
F	    -	-	31	19	-	-	27
G	    -	-	-	23	11	27	-

However, it is possible to optimise the network by removing some edges and still ensure that all points on the network remain connected. The network which achieves the maximum saving is shown below. It has a weight of 93, representing a saving of 243 − 93 = 150 from the original network.

Using network.txt (right click and 'Save Link/Target As...'), a 6K text file containing a network with forty vertices, and given in matrix form, find the maximum saving which can be achieved by removing redundant edges whilst ensuring that the network remains connected.

*****************************************
Notes:

    This version was intended to find all triangles and remove the longest side. It works for the example data but it would need to be expanded on to include squares, etc. for a complete solution. Gone with Prim's algorithm in the other version.

'''

import euler103
import time, csv

if __name__ == '__main__':
    # testing
    st = time.time()
    saveTot = 0
    inFile = list(csv.reader(open(r'./p107_network - Copy.txt')))

    for r in range(len(inFile)):
        for c in range(r,len(inFile[0]) - 1):
            #print(inFile[r][c])
            if inFile[r][c] != "-":
               for n in range(c+1, len(inFile[0])):
                   if inFile[r][n] != "-":
                       if inFile[c][n] != "-":
                           bigSide = int(max(inFile[r][c], inFile[r][n], inFile[c][n]))
                           saveTot += bigSide
                           print(r,c,n, bigSide)

    print(saveTot)

    print("euler107a took %f seconds" % (time.time() - st))
