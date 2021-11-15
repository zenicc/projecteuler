"""
Created on 10 Sept 2020
@author: Campbell

The score of a dart is determined by the number of the region that the dart lands in. A dart landing outside the red/green outer ring scores zero. The black and cream regions inside this ring represent single scores. However, the red/green outer ring and middle ring score double and treble scores respectively.

At the centre of the board are two concentric circles called the bull region, or bulls-eye. The outer bull is worth 25 points and the inner bull is a double, worth 50 points.

There are many variations of rules but in the most popular game the players will begin with a score 301 or 501 and the first player to reduce their running total to zero is a winner. However, it is normal to play a "doubles out" system, which means that the player must land a double (including the double bulls-eye at the centre of the board) on their final dart to win; any other dart that would reduce their running total to one or lower means the score for that set of three darts is "bust".

When a player is able to finish on their current score it is called a "checkout" and the highest checkout is 170: T20 T20 D25 (two treble 20s and double bull).

There are exactly eleven distinct ways to checkout on a score of 6:

D3
D1	D2
S2	D2
D2	D1
S4	D1
S1	S1	D2
S1	T1	D1
S1	S3	D1
D1	D1	D1
D1	S2	D1
S2	S2	D1

Note that D1 D2 is considered different to D2 D1 as they finish on different doubles. However, the combination S1 T1 D1 is considered the same as T1 S1 D1.

In addition we shall not include misses in considering combinations; for example, D3 is the same as 0 D3 and 0 0 D3.

Incredibly there are 42336 distinct ways of checking out in total.

How many distinct ways can a player checkout with a score less than 100?
"""
import time

alist = [0] * 61
alist[0] = 1
alist[25] = 1
alist[50] = 1
for n in range(1, 21):
    alist[n] += 1
    alist[2 * n] += 1
    alist[3 * n] += 1
# print(alist)

finishers = [2 * n for n in range(1, 21)]
finishers.append(50)


def finishes(total):
    # return the number of ways you can finish on the total passed
    noFinishes = 0
    finishList = [x for x in finishers if x <= total]
    for f in finishList:
        # print('f',f)
        balance = total - f
        # print('balance',balance)
        limit = min(balance + 1, len(alist))
        # print('limit',limit)
        for a in range(limit):
            if alist[a] > 0:
                b = balance - a
                # print('pre if',total,a,b,f)
                if b < len(alist) and b > -1 and a <= b:
                    # print(total,a,b,f)
                    noFinishes += alist[a] * alist[b]
                    if a == b and a > 1 and alist[a] * alist[b] > 1:
                        noFinishes -= 1
                        if alist[a] == 3:
                            noFinishes -= 2

            # print(a, b, finishers[n],noFinishes)

    return (noFinishes)


if __name__ == '__main__':
    # testing
    s = time.time()

    # print(finishers)
    overallTot = 0
    for total in range(100):
        subTot = finishes(total)
        print(total, subTot)
        overallTot += subTot
    print(overallTot)
    # print(finishes(167))
    print("euler109 took %f seconds" % (time.time() - s))
