import operator
import itertools
from functools import reduce
import operator

def nimGame(pile):
    # Write your code here
    return 'First' if reduce(operator.xor, pile, 0) != 0 else 'Second'

n = 2
m = [3,2,4]
print(nimGame(m))

# 7,8,14,15