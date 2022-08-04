import math
from random import seed
from numpy.random import rand
from math import *

LAMBDA = 2.5
N = 10
seed(0)

newValue2 = list(map(lambda t: ((LAMBDA ** N) * (math.e ** ((-1) * LAMBDA))) / math.factorial(N), rand(100)))

print(newValue2)

if __name__ == '__main__':
    pass
