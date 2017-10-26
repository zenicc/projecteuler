from math import sqrt
from decimal import *
getcontext().prec = 105

result=0
for i in xrange(1,101):
    temp=sum(map(int,list(str(int(Decimal(i).sqrt()*10**99)))))
    if temp>=10:
        result+=temp

print result
