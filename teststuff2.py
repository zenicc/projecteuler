numStr=["0","1","2","3","4","5","6","7","8","9"]
n = 76552
nStr = str(n)
for i in range(len(numStr)):
    if nStr.count(numStr[i]) > 1:
        for j in range(len(numStr)):
            newStr = nStr.replace(numStr[i], numStr[j])
            print(newStr)
