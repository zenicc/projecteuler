"""
Created on 17 Nov 2021
@author: Campbell




A row measuring seven units in length has red blocks with a minimum length of three units placed on it, such that any two red blocks
(which are allowed to be different lengths) are separated by at least one grey square. There are exactly seventeen ways of doing this.
p114.png

How many ways can a row measuring fifty units in length be filled?

NOTE: Although the example above does not lend itself to the possibility, in general it is permitted to mix block sizes. For example, on a row measuring eight units in length you could use red (3), grey (1), and red (4).


"""

import time


if __name__ == '__main__':
    # testing
    st = time.time()

    n = 50
    minblen = 3
    combos = [1] * (minblen) + [2] + [0] * (n - minblen)
    print(combos)
    for a in range(minblen + 1, n + 1):
        combos[a] = 2*combos[a - 1] - combos[a-2] + combos[a-4]

    print(combos)

    print(combos[n])

    print("euler114a took %f seconds" % (time.time() - st))
