from itertools import combinations

def maximumPerimeterTriangle(sticks):
    # Write your code here
    r = float('-inf')
    c = combinations(sticks, 3)
    c = list(c)
    #print(c)
    l = []
    for i in c:
        i = list(i)
        i.sort()
        if i[0]+i[1] == i[2]:
            continue
        if i[0]+i[1] > i[2] and sum(i) > r:
            r = sum(i)
            l = i
#
    return [-1] if not l else l

s = [1,1,1,3,3],[1,2,3],[1,1,1,2,3,5]
for i in s:
    print(maximumPerimeterTriangle(i))