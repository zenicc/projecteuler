'''
Created on 03 June 2015

@author: Campbell


'''
import time, iccnumbers

def polyProd(poly1,poly2):
        #multiply 2 polynomials together 
        # a + bx + cx^2 + dx^3 will be held as [a,b,c,d]
        polyOut = [0]*(len(poly1) + len(poly2))
        for a in range(0,len(poly1)):
                for b in range(0,len(poly2)):
                        polyOut[a+b] += poly1[a]*poly2[b]
        
        return polyOut
                        

if __name__=='__main__':
    #testing
        s = time.time()
        n = 55374
        polyList = [[0 for j in range(n+1)] for i in range(n)] 
        valPow = 1
        for a in range(0,n):
                b = 0
                while b <= n:
                        polyList[a][b] = 1
                        b += valPow
                valPow += 1
        listProd = polyList[0]
        for m in range(1,len(polyList)):
                listProd = polyProd(listProd,polyList[m])
                listProd = listProd[:n+1]
        print(n,listProd[n])
        print("Euler76 took %f seconds" % (time.time() - s))


    

