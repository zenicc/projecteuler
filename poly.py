# coding: utf-8

#s = time.time()
n = 5
polyList = [[0 for j in range(n+1)] for i in range(n)] 
valPow = 1
for a in range(0,n):
	#polyList[a][0] = 1
	b = 0
	while b <= n:
		polyList[a][b] = 1
		b += valPow
	valPow += 1
print(polyList)
#print("First took %f seconds" % (time.time() - s))
