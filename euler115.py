"""
Created on 28 Jan 2022
@author: Campbell



NOTE: This is a more difficult version of Problem 114.

A row measuring n units in length has red blocks with a minimum length of m units placed on it, such that any two red blocks (which are allowed to be different lengths) are separated by at least one black square.

Let the fill-count function, F(m, n), represent the number of ways that a row can be filled.

For example, F(3, 29) = 673135 and F(3, 30) = 1089155.

That is, for m = 3, it can be seen that n = 30 is the smallest value for which the fill-count function first exceeds one million.

In the same way, for m = 10, it can be verified that F(10, 56) = 880711 and F(10, 57) = 1148904, so n = 57 is the least value for which the fill-count function first exceeds one million.

For m = 50, find the least value of n for which the fill-count function first exceeds one million.


"""

import time


if __name__ == '__main__':
    # testing
    st = time.time()

    n = 10000
    minblen = 50
    combos = [1] * (minblen) + [0] * (n - minblen + 1)
    print(combos)
    for a in range(minblen, n + 1):
        combos[a] = combos[a - 1] + sum(combos[0:a - minblen]) + 1
        #print(combos, combos[a - 1], sum(combos[0:a - minblen]), combos[:a - minblen)
        if combos[a] > 1000000:
            print(a, combos[a])
            break
    print(combos)
    print(combos[n])

    print("euler115 took %f seconds" % (time.time() - st))
