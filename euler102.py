'''
Created on 22 June 2020
@author: Campbell



Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000, such that a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.

Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing the co-ordinates of one thousand "random" triangles, find the number of triangles for which the interior contains the origin.

NOTE: The first two examples in the file represent the triangles in the example given above.


'''

import time, numpy, math, csv

def containsOrigin(T1):
    axisCross=[0,0,0,0] #initialise axes as none being crossed, 0 = pos x, 1 = neg y, 2= neg x, 3 = pos y

    for coord1 in range(0,2):
        for coord2 in range(coord1 + 1,3):
            # first check if x coords are the same
            if T1[coord1][0] == T1[coord2][0]:
                if T1[coord1][0] >0:
                    axisCross[0] = 1
                else:
                    axisCross[2] = 1
                break
            # then check if y coords are the same
            if T1[coord1][1] == T1[coord2][1]:
                if T1[coord1][1] >0:
                    axisCross[3] = 1
                else:
                    axisCross[1] = 1
                break

            #calculate linear equation of triangle side as y = A*x + B
            A = (T1[coord1][1] - T1[coord2][1])/(T1[coord1][0] - T1[coord2][0])

            B = T1[coord1][1] - A*T1[coord1][0]

            #check for where the line would cross the y axis (where x = 0, ie B) and whether this lies between the points
            if min(T1[coord1][1],T1[coord2][1]) <= B <= max(T1[coord1][1],T1[coord2][1]):
                if B > 0:
                    axisCross[3] = 1
                else:
                    axisCross[1] = 1

            #check for where the line would cross the x axis (where y = 0) and whether this lies between the points
            xIntercept = -B/A
            if min(T1[coord1][0],T1[coord2][0]) <= xIntercept <= max(T1[coord1][0],T1[coord2][0]):
                if xIntercept > 0:
                    axisCross[0] = 1
                else:
                    axisCross[2] = 1

    if sum(axisCross) == 4:
        return True
    else:
        if sum(axisCross) == 3:
            print("***** aaaaaaaaaaaaaaaaaaaaaaaaaagh, 3 found!!!!!!!!!! ******")
        return False

if __name__ == '__main__':
    # testing
    st = time.time()

    inFile = list(csv.reader(open(r'./p102_triangles.txt')))
    coordsList = []
    containedCnt = 0
    notContainedCnt = 0
    for incoords in inFile:
        #print(incoords)
        coordsList.append([[int(incoords[0]), int(incoords[1])],[int(incoords[2]), int(incoords[3])],[int(incoords[4]), int(incoords[5])]])

    #print(coList)

 #   coordsList = [[[-340, 495], [-153, -910], [835, -947]],
 #                 [[-175, 41],  [-421, -714], [574, -645]]]

    for coords in coordsList:
        #print(coords)
        if containsOrigin(coords):
            containedCnt += 1
        else:
            notContainedCnt += 1

    print("******* contained count =",containedCnt)
    print("******* not contained count =",notContainedCnt)
    print("changed code in ubuntu again")

    print("euler102 took %f seconds" % (time.time() - st))
