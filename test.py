
def absolutePermutation(n, k):
    if k == 0:
        return list(range(1, n + 1))
    if n % (2 * k) != 0:
        return [-1]
    result = [0] * n
    for i in range(n):
        # i is 0-based; position is i+1
        pos = i + 1
        if (pos - 1) // k % 2 == 0:
            result[i] = pos + k
        else:
            result[i] = pos - k
    return result


A = [[2, 1], [3, 0], [3, 2], [10, 5]]
# A = [[1, 6, 5, 2, 4, 3]]

for i in A:
    print(absolutePermutation(i[0], i[1]))
