'''
Created on 18 April 2020
@author: Campbell



Comparing two numbers written in index form like 2**11 and 3**7 is not difficult, as any calculator would confirm that
2**11 = 2048 < 3**7 = 2187.

However, confirming that 632382**518061 > 519432**525806 would be much more difficult, as both numbers contain over
three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a
base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.

'''

####################################################################
# If a**b > c**d
# then log(a**b) > log(c**d)
# so b*log(a) > d*log(c)
####################################################################

import time, numpy, csv, math

st = time.time()
lineNo = 1
maxLine = 0
inFile  = list(csv.reader(open(r'./p099_base_exp.txt')))

maxCouple = [1,1]
for inCouple in inFile:
    if int(inCouple[1])*math.log(int(inCouple[0])) > int(maxCouple[1])*math.log(int(maxCouple[0])):
        maxCouple = inCouple
        maxLine = lineNo
    lineNo += 1

print(maxCouple, maxLine)

print("euler99 took %f seconds" % (time.time() - st))
