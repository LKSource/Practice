def anotherMinimaxProblem(a):
    n = len(a)
    if n <= 1:
        return 0
    if all(x == a[0] for x in a):
        return 0

    # Compute tight upper bound: max pairwise XOR
    max_xor = 0
    for i in range(n):
        for j in range(i + 1, n):
            max_xor = max(max_xor, a[i] ^ a[j])

    lo, hi = 0, max_xor
    ans = hi

    # Union-Find with path compression and union by rank
    def is_connected(threshold):
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            if rank[rx] < rank[ry]:
                parent[rx] = ry
            elif rank[rx] > rank[ry]:
                parent[ry] = rx
            else:
                parent[ry] = rx
                rank[rx] += 1
            return True

        components = n
        for i in range(n):
            for j in range(i + 1, n):
                if a[i] ^ a[j] <= threshold:
                    if union(i, j):
                        components -= 1
                        if components == 1:
                            return True
        return components == 1

    # Binary search on [0, max_xor]
    while lo <= hi:
        mid = (lo + hi) // 2
        if is_connected(mid):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1

    return ans

matrix = [
    [1, 2, 3, 4],
    [1, 2, 3],
    [3, 2, 1, 4]]

for a in matrix:
    print(anotherMinimaxProblem(a))
