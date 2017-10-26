'''
Created on 24 Oct 2010

@author: Campbell
'''
print (sum([n for n in range(2,1000000) if sum(int(i)**5 for i in str(n)) == n]))