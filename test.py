from itertools import combinations

def twoArrays(k, A, B):
    # Write your code here
    A.sort()
    B.sort(reverse=True)
    check = True
    for i in range(len(A)):
        if A[i] + B[i] < k:
            check = False
    return 'YES' if check else 'NO'

s = [[8,1],[4,2],[5,6],[3,1],[4,3]]
#s = [1, 2, 3, 4]
#k = 50
#k = 7
#s = [1,2,3,4,5,6,7,8,9,10]
#s = [7]
#for i in s:
A = [2, 1, 3]
B = [7, 8, 9]
k = 10
print(twoArrays(k, A, B))