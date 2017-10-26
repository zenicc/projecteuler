'''
Created on 2015/06/03

@author: Campbell

Euler 65 - 

Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e - see question for more info!!

'''
#import time, numbers, sys, iccnumbers, collections, itertools
import time, sys, numbers

def contFracSum(listt):
    
    if len(listt) == 2: 
    	a = listt[0]
    	b = listt[1]
    	return (a * b) + 1, b
    else:
    	a = listt[0]
    	den, num = contFracSum(listt[1:])#switch num and den to get inversion
    	return (a * den) + num, den 
            

if __name__=='__main__':
    #testing
    s = time.time()
    lista = []
    lista.append(2)
    midNum = 0
    for n in range(33):
            midNum += 2
            lista.append(1)
            lista.append(midNum)
            lista.append(1)
    #print(lista)
    num, den = contFracSum(lista)
    print(len(lista), num, den)
    print(numbers.sumDigits(num))
    print("Euler 65 took %f seconds" % (time.time() - s))

sys.exit(1)

