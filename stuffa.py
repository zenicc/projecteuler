'''
Created on 12 April 2017

@author: Campbell


stuff
'''
import time, csv
from decimal import *


if __name__=='__main__':
    #testing
        s = time.time()
        #for lim in range(5,100):
        count = 0.0
        for a in range(4):
                for b in range(4):
                       if (3.0**a + 4.0**b)%5 == 0:
                               #print a,b, (3.0**a + 4.0**b)/5, int((3.0**a + 4.0**b)/5)
                                count +=1

        print count/(16)
        print("euler83 took %f seconds" % (time.time() - s))


    

