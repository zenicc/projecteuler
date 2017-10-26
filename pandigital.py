'''
Created on 27 Dec 2011

@author: Campbell

returns the set of all pandigital integers
'''
import time

tic = time.clock()

def allPandigitals():
    numList = ["1","2","3","4","5","6","7","8","9"]
    usedList = []
    panList = []

    for a in numList:
        usedLista = list(numList)
        usedLista.remove(a)
        for b in usedLista:
            usedListb = list(usedLista)
            usedListb.remove(b)
            for c in usedListb:
                usedListc = list(usedListb)
                usedListc.remove(c)
                for d in usedListc:
                    usedListd = list(usedListc)
                    usedListd.remove(d)
                    for e in usedListd:
                        usedListe = list(usedListd)
                        usedListe.remove(e)
                        for f in usedListe:
                            usedListf = list(usedListe)
                            usedListf.remove(f)
                            for g in usedListf:
                                usedListg = list(usedListf)
                                usedListg.remove(g)
                                for h in usedListg:
                                    usedListh = list(usedListg)
                                    usedListh.remove(h)
                                    for i in usedListh:
                                        newNum = str(a+b+c+d+e+f+g+h+i)
                                        panList += newNum
                                        print(panList)
                

    return panList

if __name__=='__main__':
    #testing

    tic = time.clock()
    
    
    print (allPandigitals())

    print("Time elapsed =", time.clock() - tic)

