from itertools import permutations


def absolutePermutation(n, k):
    # Write your code here
    p = list(range(1, n + 1))
    P = list(permutations(p, n))
    for v in P:
        check = True
        # print(v)
        for i in range(len(v)):
            # print(v[i], v[i] - (i+1))
            if abs(v[i] - (i+1)) != k:
                check = False
                break
        if check:
            return v
    return -1


A = [[2, 1], [3, 0], [3, 2]]
# A = [[1, 6, 5, 2, 4, 3]]

for i in A:
    print(absolutePermutation(i[0], i[1]))
