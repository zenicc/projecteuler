'''
Created on 28 Dec 2019
@author: Campbell



Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept. Its origin is unclear, but credit
 must be attributed to Leonhard Euler who invented a similar, and much more difficult, puzzle idea called Latin Squares.
The objective of Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row,
column, and 3 by 3 box contains each of the digits 1 to 9. Below is an example of a typical starting puzzle grid and its
solution grid.

0 0 3	0 2 0 	6 0 0
9 0 0   3 0 5   0 0 1
0 0 1   8 0 6   4 0 0

0 0 8 	1 0 2 	9 0 0
7 0 0   0 0 0   0 0 8
0 0 6   7 0 8   2 0 0

0 0 2 	6 0 9 	5 0 0
8 0 0   2 0 3   0 0 9
0 0 5   0 1 0   3 0 0

--------------------------

4 8 3 	9 2 1 	6 5 7
9 6 7   3 4 5   8 2 1
2 5 1   8 7 6   4 9 3

5 4 8 	1 3 2 	9 7 6
7 2 9   5 6 4   1 3 8
1 3 6   7 9 8   2 4 5

3 7 2 	6 8 9 	5 1 4
8 1 4   2 5 3   7 6 9
6 9 5   4 1 7   3 8 2

A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary to
employ "guess and test" methods in order to eliminate options (there is much contested opinion over this). The complexity
of the search determines the difficulty of the puzzle; the example above is considered easy because it can be solved by
straight forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles ranging
in difficulty, but all with unique solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid; for
example, 483 is the 3-digit number found in the top left corner of the solution grid above.

'''

import time, csv, math, sudoku

import numpy

def solvePuzz(inPuzz):
    puzz = [[[] for _ in range(10)] for _ in range(10)]
    for n in range(1, 10):
        for m in range(1,10):
            c = inPuzz[n][m][0]
            if c == 0:
                puzz[n][m] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            else:
                puzz[n][m] = [int(c)]
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


if __name__=='__main__':

    st = time.time()

    T1 = list(csv.reader(open(r'./p096_sudoku.txt')))
    newPuzz = [[[] for _ in range(10)] for _ in range(10)]

    total = 0
    for puzzNum in range(50):
        for n in range(1, 10):
            for m in range(len(T1[n][0])):
                newPuzz[n][m + 1] = [int(T1[10*puzzNum + n][0][m])]

        #print(newPuzz)
        puzz = sudoku.solvePuzzle(newPuzz)
        subTot = 100*puzz[1][1][0] + 10*puzz[1][2][0] + puzz[1][3][0]
        total += subTot
        print("************* puzzle ",puzzNum + 1," *************" )
        for m in range(1,10):
            for n in range(1,9):
                print('%-12r' % puzz[m][n], end='\t')
            print('%-12r' % puzz[m][9])
        print("subTot = ", subTot)
        print("total = ", total)
        if sum(numpy.sum(puzz)) == 405:
            print("complete")
        else:
            print("*** not finished ***")
        print()

    print("euler96 took %f seconds" % (time.time() - st))
