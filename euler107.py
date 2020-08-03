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

    Use Prim's algorithm?

'''

import time, csv, numpy

def getNextVert(fList, iList, iFile):
    minVertSize = numpy.inf

    for f in fList:
        for g in iList:
            if iFile[f][g] < minVertSize:
                minVertSize  = iFile[f][g]
                minVert = [f, g]
    return minVert, minVertSize




if __name__ == '__main__':
    # testing
    st = time.time()

    verticeTot = 0
    inTot = 0
    inFile = list(csv.reader(open(r'./p107_network.txt')))

    for inList in inFile:
        inTot += sum([0 if x == '-' else int(x) for x in inList])
        inList[:] = [numpy.inf if x == '-' else int(x) for x in inList]

    verticeList = []
    doneList = []
    frontList = []
    inList = [i for i in range(len(inFile))]

    frontList.append(0)
    inList.remove(0)

    print(doneList)
    print(frontList)
    print(inList)

    while len(inList) > 0:
        vertice, verticeLen  = getNextVert(frontList, inList, inFile)
        verticeTot += verticeLen
        #print("moving ", vertice[1],"to frontier from ",vertice[0], "with value",verticeLen)
        frontList.append(vertice[1])
        inList.remove(vertice[1])
        inFile[vertice[0]][vertice[1]] = numpy.inf
        inFile[vertice[1]][vertice[0]] = numpy.inf
        verticeList.append(vertice)
        # the following is to reduce the size of the frontList - actually makes performance slightly worse for this size data but might be good for bigger datasets
        for f in frontList:
            Move = True
            for g in range(len(inFile[f])):
                if inFile[f][g] < numpy.inf and g in inList:
                    Move = False
            if Move:
                doneList.append(f)
                frontList.remove(f)

    print("*************** vertice tot = ", verticeTot)
    print("*************** in tot = ", inTot/2)
    print("*************** answer = ", inTot/2 - verticeTot)
    print("********************************************")
    print("doneList",doneList)
    print("frontList",frontList)
    print("inList",inList)
    print("verticeList",verticeList)



    print("euler107 took %f seconds" % (time.time() - st))
