'''
Created on 28 Dec 2019
@author: Campbell





'''

import time, csv, math

import numpy

def solvePuzzLogical(inPuzz):
    # solve puzzle logically as far as possible - could do more things here but overcomplicating the code
    puzz = [[[] for _ in range(10)] for _ in range(10)]
    for n in range(1, 10):
        for m in range(1,10):
            c = inPuzz[n][m][0]
            if c == 0:
                puzz[n][m] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            else:
                #puzz[n][m] = [int(c)]
                puzz[n][m] = inPuzz[n][m]
    changed = True
    while changed:
        changed = False
        for m in range(1, 10):
            for n in range(1, 10):
                if len(puzz[m][n]) > 1:
                    # print(m,n,puzz[m][n])
                    # check columns and rows
                    for r in range(1, 10):
                        if len(puzz[m][r]) == 1 and len(puzz[m][n]) > 1 and len(set(puzz[m][r]) - set(puzz[m][n])) == 0:
                            # print('   ',m,r,puzz[m][r])
                            puzz[m][n] = list(set(puzz[m][n]) - set(puzz[m][r]))
                            changed = True
                        if len(puzz[r][n]) == 1 and len(puzz[m][n]) > 1 and len(set(puzz[r][n]) - set(puzz[m][n])) == 0:
                            puzz[m][n] = list(set(puzz[m][n]) - set(puzz[r][n]))
                            changed = True

                    # check subsquare
                    subr = 3 * int((m - 1) / 3) + 1
                    subc = 3 * int((n - 1) / 3) + 1
                    for r in range(subr, subr + 3):
                        for c in range(subc, subc + 3):
                            if len(puzz[r][c]) == 1 and len(puzz[m][n]) > 1 and len(set(puzz[r][c]) - set(puzz[m][n])) == 0:
                                puzz[m][n] = list(set(puzz[m][n]) - set(puzz[r][c]))
                                changed = True
        for m in range(1, 10):
            for n in range(1, 10):
                # check for number unique in row
                if len(puzz[m][n]) > 1:
                    for a in puzz[m][n]:
                        numFound = False
                        for r in range(1,10):
                            if not(r == n):
                                if a in puzz[m][r]:
                                    numFound = True
                                    break
                        if not numFound:
                            puzz[m][n] = [a]
                            changed = True
                            break
                # check for number unique in column
                if len(puzz[m][n]) > 1:
                    for a in puzz[m][n]:
                        numFound = False
                        for r in range(1,10):
                            if not(r == m):
                                if a in puzz[r][n]:
                                    numFound = True
                                    break
                        if not numFound:
                            puzz[m][n] = [a]
                            changed = True
                            break
                # check for number unique in 3 x 3 block
                if len(puzz[m][n]) > 1:
                    for a in puzz[m][n]:
                        numFound = False
                        subr = 3 * int((m - 1) / 3) + 1
                        subc = 3 * int((n - 1) / 3) + 1
                        for r in range(subr, subr + 3):
                            for c in range(subc, subc + 3):
                                if not(r == m and c == n):
                                    if a in puzz[r][c]:
                                        numFound = True
                                        break
                        if not numFound:
                            puzz[m][n] = [a]
                            changed = True
                            break
        for m in range(1, 10):
            for n in range(1, 10):
                if len(puzz[m][n]) == 2:
                    for c in range(n+1,10):
                        if set(puzz[m][n]) == set(puzz[m][c]):
                            for x in range(1,10):
                                diff = len(set(puzz[m][x]) - set(puzz[m][n]))
                                if not(diff == 0) and not(diff == len(set(puzz[m][x]))):
                                    puzz[m][x] = list(set(puzz[m][x]) - set(puzz[m][n]))
                                    changed = True
                    for r in range(m+1,10):
                        if set(puzz[m][n]) == set(puzz[r][n]):
                            for y in range(1,10):
                                diff = len(set(puzz[y][n]) - set(puzz[m][n]))
                                if not(diff == 0) and not(diff == len(set(puzz[y][n]))):
                                    puzz[y][n] = list(set(puzz[y][n]) - set(puzz[m][n]))
                                    changed = True

                    # check subsquare
                    subr = 3 * int((m - 1) / 3) + 1
                    subc = 3 * int((n - 1) / 3) + 1
                    for r in range(subr, subr + 3):
                        for c in range(subc, subc + 3):
                            if set(puzz[m][n]) == set(puzz[r][c]) and not(r == m and c == n):
                                subr1 = 3 * int((m - 1) / 3) + 1
                                subc1 = 3 * int((n - 1) / 3) + 1
                                for r1 in range(subr1, subr1 + 3):
                                    for c1 in range(subc1, subc1 + 3):
                                        diff = len(set(puzz[r1][c1]) - set(puzz[m][n]))
                                        if not(diff == 0) and not(diff == len(set(puzz[r1][c1]))):
                                            puzz[r1][c1] = list(set(puzz[r1][c1]) - set(puzz[m][n]))
                                            changed = True

        for m in range(1, 10):
            for n in range(0, 3):
                for a in list(set(puzz[m][3 * n + 1] + puzz[m][3 * n + 2] + puzz[m][3 * n + 3])):
                    n0 = list(set([0, 1, 2]) - set([n]))
                    n1 = n0[0]
                    n2 = n0[1]
                    if a not in list(set(puzz[m][3 * n1 + 1] + puzz[m][3 * n1 + 2] + puzz[m][3 * n1 + 3]
                                     + puzz[m][3 * n2 + 1] + puzz[m][3 * n2 + 2] + puzz[m][3 * n2 + 3])):
                        subr = 3 * int((m - 1) / 3) + 1
                        subc = 3 * n + 1
                        for r in range(subr, subr + 3):
                            for c in range(subc, subc + 3):
                                if not (r == m) and a in puzz[r][c] and len(puzz[r][c]) > 1:
                                    puzz[r][c] = list(set(puzz[r][c]) - set([a]))
                                    changed = True

        for n in range(1, 10):
            for m in range(0, 3):
                for a in list(set(puzz[3 * m + 1][n] + puzz[3 * m + 2][n] + puzz[3 * m + 3][n])):
                    m0 = list(set([0, 1, 2]) - set([m]))
                    m1 = m0[0]
                    m2 = m0[1]
                    if a not in list(set(puzz[3 * m1 + 1][n] + puzz[3 * m1 + 2][n] + puzz[3 * m1 + 3][n]
                                     + puzz[3 * m2 + 1][n] + puzz[3 * m2 + 2][n] + puzz[3 * m2 + 3][n])):
                        subr = 3 * m + 1
                        subc = 3 * int((n - 1) / 3) + 1
                        for r in range(subr, subr + 3):
                            for c in range(subc, subc + 3):
                                if not (c == n) and a in puzz[r][c] and len(puzz[r][c]) > 1:
                                    puzz[r][c] = list(set(puzz[r][c]) - set([a]))
                                    changed = True

    return puzz

def puzzSolved(inPuzz):
    # check whether solution passed is valid
    solved = True
    if not(sum(numpy.sum(inPuzz)) == 405):
        return False
    else:
        colVal = numpy.sum(inPuzz, axis = 1)
        rowVal = numpy.sum(inPuzz, axis = 0)
        for m in range(1, 10):
            if not(sum(colVal[m]) == 45):
                return False
            if not(sum(rowVal[m]) == 45):
                return False
    return True

def solvePuzzle(inPuzz):
    # first try to solve puzzle passed logically but posit if necessary

    tryPuzz = [[[], [], [], [], [], [], [], [], [], []],
               [[], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
               [[], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
               [[], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
               [[], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
               [[], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
               [[], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
               [[], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
               [[], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
               [[], [0], [0], [0], [0], [0], [0], [0], [0], [0]]]

    puzz = solvePuzzLogical(inPuzz)

    if puzzSolved(puzz):
        return puzz

    for m in range(10):
        for n in range(10):
            tryPuzz[m][n] = puzz[m][n]

    for m in range(10):
        for n in range(10):
            if len(puzz[m][n]) > 1:
                for positNo in range(len(puzz[m][n])):
                    tryPuzz[m][n] = [puzz[m][n][positNo]]
                    tryPuzzSolve = solvePuzzLogical(tryPuzz)
                    if puzzSolved(tryPuzzSolve):
                        return tryPuzzSolve

    return 1





if __name__=='__main__':

    st = time.time()

    newPuzz = [[[],[],[],[],[],[],[],[],[],[]],
               [[],[3],[0],[0],[2],[0],[0],[0],[0],[0]],
               [[],[0],[0],[0],[1],[0],[7],[0],[0],[0]],
               [[],[7],[0],[6],[0],[3],[0],[5],[0],[0]],
               [[],[0],[7],[0],[0],[0],[9],[0],[8],[0]],
               [[],[9],[0],[0],[0],[2],[0],[0],[0],[4]],
               [[],[0],[1],[0],[8],[0],[0],[0],[5],[0]],
               [[],[0],[0],[9],[0],[4],[0],[3],[0],[1]],
               [[],[0],[0],[0],[7],[0],[2],[0],[0],[0]],
               [[],[0],[0],[0],[0],[0],[8],[0],[0],[6]]]

    solvedPuzz = solvePuzzle(newPuzz)

    for m in range(1, 10):
        for n in range(1, 9):
            print('%-12r' % solvedPuzz[m][n], end='\t')
        print('%-12r' % solvedPuzz[m][9])
    print()

    print("sudoku took %f seconds" % (time.time() - st))


'''
    tryPuzz = [[[], [], [], [], [], [], [], [], [], []],
               [[], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
               [[], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
               [[], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
               [[], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
               [[], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
               [[], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
               [[], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
               [[], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
               [[], [0], [0], [0], [0], [0], [0], [0], [0], [0]]]

    puzz = solvePuzz(newPuzz)
    print("************* puzzle  *************")
    for m in range(1, 10):
        for n in range(1, 9):
            print('%-12r' % puzz[m][n], end='\t')
        print('%-12r' % puzz[m][9])
    if puzzSolved(puzz):
        print("complete")
    else:
        change = False
        for m in range(10):
            for n in range(10):
                tryPuzz[m][n] = puzz[m][n]
                if len(puzz[m][n]) > 1 and change == False:
                    tryPuzz[m][n] = [puzz[m][n][0]]
                    change = True

    print("************* puzzle  *************")
    for m in range(1, 10):
        for n in range(1, 9):
            print('%-12r' % tryPuzz[m][n], end='\t')
        print('%-12r' % tryPuzz[m][9])
    print()
    trypuzzSolve = solvePuzz(tryPuzz)
    print("************* puzzle  *************")
    for m in range(1, 10):
        for n in range(1, 9):
            print('%-12r' % trypuzzSolve[m][n], end='\t')
        print('%-12r' % trypuzzSolve[m][9])
    if puzzSolved(trypuzzSolve):
        print("complete")
    else:
        print("Oh dear oh dear")
'''
