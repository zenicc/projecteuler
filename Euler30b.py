'''
Created on 24 Oct 2010

@author: Campbell

Returns those numbers where the individual digits of the number raised to the power 5 sum to equal the number
Note that 999999 with each digit raised to 5 gives 354294 so all numbers that satisfy the condition must be < 354294
'''
total = 0
for n in range(2,354294):
    if sum(int(i)**5 for i in str(n)) == n:
        print(n)
        total += n
print ("Total is", total) 
        