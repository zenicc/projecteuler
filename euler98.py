'''
Created on 18 April 2020
@author: Campbell



By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: 1296 = 36**2.

What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square number:
9216 = 96**2. We shall call CARE (and RACE) a square anagram word pair and specify further that leading zeroes are not
permitted, neither may a different letter have the same digital value as another letter.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common
English words, find all the square anagram word pairs (a palindromic word is NOT considered to be an anagram of itself).

What is the largest square number formed by any member of such a pair?

NOTE: All anagrams formed must be contained in the given text file.

'''
# Note that although this gives a correct result it also gives some wrong answers as it does not distinguish where a
# square has a different arrangement of duplicate digits eg it matches FORMER to 675684 although the duplicate Rs don't
# line up with the duplicate 6s
import time, numpy, csv
from collections import Counter

st = time.time()

inFile  = list(csv.reader(open(r'./p098_words.txt')))[0]

maxWordLen = len(max(inFile, key=len))
wordList = [[]for _ in range(maxWordLen + 1)]
pairList = []
############################################
# get list of anagram pairs
############################################

for word in inFile:
    wordList[len(word)].append(word)

for n in range(maxWordLen + 1):
    for m in range(len(wordList[n])):
        counterWord = Counter(wordList[n][m])
        for p in range(m+1, len(wordList[n])):
            if counterWord == Counter(wordList[n][p]):
                pairList.append([wordList[n][m], wordList[n][p]])
############################################

############################################
# get all squares into a list by length of square
############################################

squares = [[] for _ in range(10)]
for n in range(1,31622):
    square = n*n
    squares[len(str(square))].append(square)
#############################################

for nums in pairList:

    ######################################################
    # start of loop to deal with one pair of anagrams
    ######################################################
    anaMap = []
    for n in range(len(nums[1])):
        anaMap.append(nums[0].find(nums[1][n]))

    # print(anaMap)
    # print(squares)

    for n in squares[len(nums[0])]:  # the squares being looked at must be the same length as the anagram
        # check the square number has the same count of distinct digits as the word - this is where the possible mismatch
        # of ordering of repeated characters mentioned at the start is not dealt with and would have to be coded ideally.
        if len(Counter(str(n))) == len(Counter(nums[0])):
            numStr = str(n)
            anaNumStr = ''
            for dig in range(len(numStr)):
                anaNumStr += numStr[anaMap[dig]]
            anaNumRoot = int(anaNumStr) ** .5
            if anaNumRoot.is_integer() and not (anaNumStr[0] == "0"):
                print(nums[0], n, nums[1], int(anaNumStr))

    ######################################################
    # end of loop to deal with one pair of anagrams
    ######################################################

print("euler98 took %f seconds" % (time.time() - st))
