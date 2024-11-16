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

    n = 8

    singles = (n**2 - 3*n + 4) / 2

    coeff = 1
    combos = 0

    for a in range(5):
        combos += (5 - a) * coeff
        coeff = coeff * (n - 9 + a + 1) / (a + 1)

    print(singles, combos, singles + combos)

    print("euler114 took %f seconds" % (time.time() - st))
