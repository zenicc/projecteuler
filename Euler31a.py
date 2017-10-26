'''
Created on 27 Oct 2010
Gives all ways that £2 can be made up from coins

@author: Campbell
'''
@Cached
def nway( total, coins):
    if not coins: return 0
    c, coins = coins[0], coins[1:]
    count = 0 
    if total % c == 0: count += 1    
    for amount in xrange( 0, total, c):
        count += nway(total - amount, coins)    
    return count
# main
print nway( 200, (1,2,5,10,20,50,100,200))