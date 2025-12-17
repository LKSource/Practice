import operator
import itertools

def gameOfStones(n):
    # Write your code here
    #print(n)
    if n % 7 in (0, 1):
        return 'Second'
    else:
        return 'First'

s = [7,8,14,15,9,10,11,12,13]
#s = [14, 15]
for i in s:
    print(gameOfStones(i))

# 7,8,14,15