from fractions import Fraction
from functools import reduce
from itertools import product
from operator import mul

print(reduce(mul, \
             [Fraction(a,c) for a,b,c in product(range(1,10), repeat=3) \
              if Fraction(a,c) == Fraction(10*a+b, 10*b+c)]))
