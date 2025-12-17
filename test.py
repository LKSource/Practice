from itertools import combinations

def lonelyinteger(a):
    # Write your code here
    result = [r for r in a if a.count(r)==1]
    return result[0]

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
print(lonelyinteger(B))