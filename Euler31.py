'''
Created on 27 Oct 2010
Gives all ways that £2 can be made up from coins
Brute force solution. Very slow - see 31b for a faster version of the same idea
@author: Campbell
'''
target = 200
count = 0
for c200 in range(int(target/200) + 1):
    for c100 in range(int(target/100) + 1):
        for c50 in range(int(target/50) + 1):
            for c20 in range(int(target/20) + 1):
                for c10 in range(int(target/10) + 1):
                    for c5 in range(int(target/5) + 1):
                        for c2 in range(int(target/2) + 1):
                            for c1 in range(target + 1):
                                total = (200*c200) + (100*c100) + (50*c50) + (20*c20) + (10*c10) + (5*c5) + (2 * c2) + c1
                                if total == target:
                                    count += 1
                                    print (c200, c100, c50, c20, c10, c5, c2, c1)
                                    print (total)
print ("count",count)