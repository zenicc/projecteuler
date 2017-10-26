'''
Created on 16 Dec 2012

@author: Campbell

Euler 54 - Determine poker winning hands 
'''
import time
from pokerhand import rankPokerhand

tic = time.clock()

count1 = 0

with open("poker.txt") as f:
    content = f.readlines()
    
for line in range(len(content)):
    hand1 = []
    hand2 = []

    for i in range(0,13,3):
        hand1.append(content[line][i] + content[line][i+1])

    for i in range(15,28,3):
        hand2.append(content[line][i] + content[line][i+1])
    hand1rank, hand1val = rankPokerhand(hand1)
    hand2rank, hand2val = rankPokerhand(hand2)
    #print(hand1,hand1rank,hand1val)
    #print(hand2,hand2rank,hand2val)
    if hand1rank < hand2rank:
        count1 = count1 + 1
    elif (hand1rank == hand2rank) and (hand1val > hand2val):
        count1 = count1 + 1

print(count1)
print("Time elapsed =", time.clock() - tic)
