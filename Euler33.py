'''
Created on 21 Dec 2011

@author: Campbell

'''
import time
import fractions

tic = time.clock()
numtot = 1
dentot = 1
for num in range(99):
    for den in range(99):
        if (num%10 == den//10) \
            and den%10 > 0 \
            and num//10 > 0 \
            and num != den \
            and ((num//10)/(den%10) == num/den):
                print (num,"/", den)
                numtot = numtot*num
                dentot = dentot*den
print ("numerator =", numtot)
print ("denominator =", dentot)
print ("fraction is ", fractions.Fraction(numtot, dentot))
print ("time elapsed: ", time.clock() - tic)
    
