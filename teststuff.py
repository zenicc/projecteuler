import numbers

numStr=["0","1","2","3","4","5","6","7","8","9"]
n = 1000000
pList = numbers.getPrimes(n)
newList = []
for a in range(len(pList)):
    nStr = str(pList[a])
    for i in range(len(numStr)):
        if nStr.count(numStr[i]) > 1:
            count = 0
            for j in range(i,len(numStr)):
                newStr = nStr.replace(numStr[i], numStr[j])
                if numbers.isPrime(newStr):
                    count = count + 1
            if count > 7:
                print(nStr)
