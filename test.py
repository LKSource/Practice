def permute(arr):
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [arr]
    res = []
    for i in range(len(arr)):
        elem = arr[i]
        rem = arr[:i] + arr[i+1:]
        for p in permute(rem):
            res.append([elem] + p)
    return res


def anotherMinimaxProblem(a):
    # Write your code here
    r = []
    for p in permute(a):
        r.append(max([p[i] ^ p[i+1] for i in range(len(p)-1)]))
    return min(r)

matrix = [
    [1, 2, 3, 4],
    [1, 2, 3],
    [3, 2, 1, 4]]

for a in matrix:
    print(anotherMinimaxProblem(a))
