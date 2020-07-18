aSize = 50
outArray=[[0 for i in range(aSize)] for j in range(aSize)]
for u in range(1, 5):
    for v in range(u+1, 5):
        a = v*v - u*u
        b = 2*u*v
        c = v*v + u*u
        outArray[a][b] = c
        outArray[b][a] = c
        print(a, b, c)
        n = 2
        while a*n <= aSize and b*n <= aSize:
            outArray[n*a][n*b] = n*c
            outArray[n*b][n*a] = n*c
            n += 1

for x in range(aSize):
    print(outArray[x])