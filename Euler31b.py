'''
Created on 27 Oct 2010

Gives all ways that £2 can be made up from coins
@author: Campbell
'''
target = 200
count = 0
for c200 in range(int(target/200) + 1):
    if c200*200 > 200: break
    for c100 in range(int(target/100) + 1):
        if c200*200 + c100*100 > 200: break
        for c50 in range(int(target/50) + 1):
            if c200*200 + c100*100 + c50*50 > 200: break
            for c20 in range(int(target/20) + 1):
                if c200*200 + c100*100 + c50*50 + c20*20 > 200: break
                for c10 in range(int(target/10) + 1):
                    if c200*200 + c100*100 + c50*50 + c20*20 + c10*10 > 200: break
                    for c5 in range(int(target/5) + 1):
                        if c200*200 + c100*100 + c50*50 + c20*20 + c10*10 + c5*5 > 200: break
                        for c2 in range(int(target/2) + 1):
                            if c200*200 + c100*100 + c50*50 + c20*20 + c10*10 + c5*5 + c2*2 > 200: break
                            for c1 in range(target + 1):
                                if c200*200 + c100*100 + c50*50 + c20*20 + c10*10 + c5*5 + c2*2 + c1 > 200: break
                                total = (200*c200) + (100*c100) + (50*c50) + (20*c20) + (10*c10) + (5*c5) + (2 * c2) + c1
                                if total == target:
                                    count += 1
print ("count",count)