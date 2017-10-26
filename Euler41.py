'''
Created on 1 Jan 2012

@author: Campbell

Euler 41 - count triangle words in file
'''
import time
import string

def getTriangleNos(limit):
    triList = list()
    for n in range(10000):
        triNo = (n/2)*(n+1)
        triList.append(int(triNo))
        if triNo > limit:
            return triList

    return triList
    

tic = time.clock()

triNoList = getTriangleNos(200)
#print (triNoList)


with open("words.txt","r") as f:
    inData = f.read().replace('"','').split(",")
f.closed

    
wordCount = 0

for wordStr in inData:
    tot = sum(ord(letter) - 64 for letter in wordStr)
    if tot in triNoList:
        #print (wordStr, tot)
        wordCount += 1

print ("Word count =", wordCount)
    
print("Time elapsed =", time.clock() - tic)

