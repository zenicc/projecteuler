import time

s = time.time()
penta = sum([[x*(3*x - 1)/2, x*(3*x - 1)/2 + x] for x in range(1, 250)], [])
p, sgn, n, limit  = [1], [1, 1, -1, -1], 0, 1e6

while p[n]>0:
    n += 1
    px, i = 0, 0
    while penta[i] <= n:
        px += p[n - penta[i]] * sgn[i%4]
        i += 1
    p.append(px % limit)

print (n)
print("Took %f seconds" % (time.time() - s))
