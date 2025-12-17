import operator
import itertools

def towerBreakers(n, m):
    # Write your code here
    if m == 1:
        return 2
    else:
        return 1 if n % 2 == 1 else 2

n = 2
m = 2
print(towerBreakers(n, m))

# 7,8,14,15