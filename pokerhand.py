'''
Created on 16 Dec 2012

@author: Campbell

Part of Euler 53 - rank poker hand
'''
import time

def rankPokerhand(handIn):

    values = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
    handSuit = []
    handValue = []
    for i in range(len(values)):
        for j in range(len(handIn)):
            if handIn[j][0] == values[i]:
                handValue.append(values.index(values[i]))
                handSuit.append(handIn[j][1])
    rank = 0
    val = 0
    
    if handSuit[0] == handSuit[1] == handSuit[2] == handSuit[3] == handSuit[4]:
        if handValue[4] == handValue[3] + 1 and \
           handValue[3] == handValue[2] + 1 and \
           handValue[2] == handValue[1] + 1 and \
           handValue[1] == handValue[0] + 1:#straight flush
            rank = 1
            val = handValue[4]
            return rank, val 
        else:#flush
            rank = 4
            val = handValue[4]
            return rank, val 

    if handValue[4] == handValue[3] + 1 and \
        handValue[3] == handValue[2] + 1 and \
        handValue[2] == handValue[1] + 1 and \
        handValue[1] == handValue[0] + 1: #straight
            rank = 5
            val = handValue[4]
            return rank, val
        
    for i in range(len(handValue)):
        if handValue.count(handValue[i]) == 4:#4 of a kind
            rank = 2
            val = i
            return rank, val 
        if handValue.count(handValue[i]) == 3:
            if rank == 8:#already found a pair so full house
                rank = 3
                val = val + 10*handValue[i]
                return rank, val
            else:
                if rank == 0:#trio found
                    rank = 6
                    val = 10*handValue[i]
        if handValue.count(handValue[i]) == 2:
            if rank == 8 and val != handValue[i]:#already found a pair so 2 pairs
                rank = 7
                val = val + 10*handValue[i]
                return rank, val
            else:
                if rank == 6:#already found a trio so full house
                    rank = 3
                    val = val + handValue[i]
                    return rank, val
                else:
                    if rank == 0:#pair found
                        rank = 8
                        val = handValue[i]
        if i == 4 and rank > 0:#pair or trio only
            return rank, val
    return 9, handValue[4]#high card only
            


if __name__=='__main__':
    #testing
    s = time.time()
    h = ["3C","3C","3D","8S","5H"] 
    print(rankPokerhand(h))
    print("Took %f seconds" % (time.time() - s))

