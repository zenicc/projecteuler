'''
Created on 28 April 2020
@author: Campbell



If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken
at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing
eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 10**12 = 1,000,000,000,000 discs in total, determine the number of blue
discs that the box would contain.

'''

########################################################################################################
# Can't find the problem with my solution below which appears correct but Proj Euler rejects.
# I think it is a problem with the floating point arithmetic.
# I also note that their solution of 85 B and 35 R sometimes fails to be probability 0.5 depending how you arrange the
# formula!
########################################################################################################

import time, numpy, math

st = time.time()

rangeStart = 10**12
rangeEnd = rangeStart + 10000000

for totalDiscs in range(rangeStart,rangeEnd):
    lowerR = int(totalDiscs*(1.0/(2**.5))) - 10
    if ((lowerR/totalDiscs)*((lowerR-1.0)/(totalDiscs-1.0))) >= 0.5:
        print("greater than 0.5", totalDiscs)
    for b in range(lowerR,totalDiscs):
        r = totalDiscs - b
        prob = (b/totalDiscs)*((b-1.0)/(totalDiscs-1.0))
        if b == 85 and totalDiscs == 120:
            print(totalDiscs,b,r,b/totalDiscs,prob)

        if prob == 0.5:
            print('*****************************************')
            print(totalDiscs,b,r,b/totalDiscs,prob)
            print('*****************************************')
            exit()
        if prob >= 0.5:
            #print(totalDiscs,b,r,b/totalDiscs,prob)
            break

print("euler100 took %f seconds" % (time.time() - st))
