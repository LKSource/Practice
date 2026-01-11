def twoPluses(grid):
    H = len(grid)
    W = len(grid[0])
    # Convert to binary: 1 for 'G', 0 for 'B'
    mat = [[1 if ch == "G" else 0 for ch in row] for row in grid]
    # For each cell, compute max arm length (k)
    # k = 0 -> only center; k = 1 -> center + 1 in each direction, etc.
    max_k = [[0] * W for _ in range(H)]
    for r in range(H):
        for c in range(W):
            if mat[r][c] == 0:
                max_k[r][c] = -1  # invalid
                continue
            k = 0
            # Try to expand arms
            while True:
                # Check if we can extend to arm length k+1
                if (
                    r - k - 1 >= 0
                    and r + k + 1 < H
                    and c - k - 1 >= 0
                    and c + k + 1 < W
                    and mat[r - k - 1][c] == 1
                    and mat[r + k + 1][c] == 1
                    and mat[r][c - k - 1] == 1
                    and mat[r][c + k + 1] == 1
                ):
                    k += 1
                else:
                    break
            max_k[r][c] = k

    # Build list of all pluses: (area, set_of_cells)
    pluses = []
    for r in range(H):
        for c in range(W):
            if max_k[r][c] >= 0:
                # For each possible arm length from 0 up to max_k[r][c]
                # Because a plus with max arm k can also be used as smaller
                # plus!
                for k in range(0, max_k[r][c] + 1):
                    area = 1 + 4 * k
                    cells = {(r, c)}
                    for d in range(1, k + 1):
                        cells.add((r - d, c))
                        cells.add((r + d, c))
                        cells.add((r, c - d))
                        cells.add((r, c + d))
                    pluses.append((area, cells))

    # Now find max product of two non-overlapping pluses
    max_product = 0
    n = len(pluses)
    for i in range(n):
        for j in range(i + 1, n):
            area1, cells1 = pluses[i]
            area2, cells2 = pluses[j]
            if cells1.isdisjoint(cells2):
                max_product = max(max_product, area1 * area2)

    return max_product


g = ["GGGGGG", "GBBBGB", "GGGGGG", "GGBBGB", "GGGGGG"]

g1 = ["BGBBGB", "GGGGGG", "BGBBGB", "GGGGGG", "BGBBGB", "BGBBGB"]

print(twoPluses(g))
