# from itertools import permutations

def larrysArray(A):
    count = 0
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if A[i] > A[j]:
                count += 1
    return "YES" if count % 2 == 0 else "NO"


A = [[3, 1, 2], [1, 3, 4, 2], [1, 2, 3, 5, 4], [1, 6, 5, 2, 4, 3]]
# A = [[1, 6, 5, 2, 4, 3]]

for i in A:
    print(larrysArray(i))
