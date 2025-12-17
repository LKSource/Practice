import operator
import itertools

def maximizingXor(l, r):
    # Write your code here
    lst = []
    for i in range(l,r+1):
        lst += [i]
    plst = list(itertools.permutations(lst, r=2))
    result = 0
    for i in plst:
        t = operator.xor(i[0],i[1])
        if t > result:
            result = t
    return result

s = [[8,1],[4,2],[5,6],[3,1],[4,3]]
#s = [1, 2, 3, 4]
#k = 50
#k = 7
#s = [1,2,3,4,5,6,7,8,9,10]
#s = [7]
#for i in s:
A = [2, 1, 3]
B = [0,0,1,2,1]
k = 10
l = 10
r = 15
print(maximizingXor(l,r))