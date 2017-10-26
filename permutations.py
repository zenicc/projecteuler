'''
Created on 28 Dec 2011

@author: Campbell

returns list of all permutations of inList items as strings
'''
import time
from itertools import permutations

tic = time.clock()

def allPermsAsStrs(inList):
    "returns list of all perms of inList as strings"
    
    permList = []
    
    for perms in list(permutations(inList)):
        permList.append(str("".join(perms)))

    return permList

def anagram(inStr):
    "returns a list of all anagrams of a given string"
    wordList = []
    inList = []
    inList += inStr
    return allPermsAsStrs(inList)
    

if __name__=='__main__':
    #testing

    tic = time.clock()

    inWord = "123456789"
    numList = [n for n in anagram(inWord) if int(n) > 912311111]
    smallList = [n for n in numList if (int(n[2:4]) == 2*int(n[0:2]))\
                 or (int(n[2:5]) == 2*int(n[0:2]))\
                 or (int(n[4:]) == 2*int(n[0:4]))]
    smallList.sort(reverse=True)
    print (smallList)
    print (len(smallList))
    
    
   
    #numList = ["1","2","3","4","5","6","7","8","9"]
    
    #permListO = allPermsAsStrs(numList)
    #print (len(permListO))

    print("Time elapsed =", time.clock() - tic)

