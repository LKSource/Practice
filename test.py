def matrixRotation(matrix, r):
    m = len(matrix)
    n = len(matrix[0])
    layers = min(m, n) // 2

    for layer in range(layers):
        ring = []
        # Left column: top to bottom
        for i in range(layer, m - layer):
            ring.append(matrix[i][layer])
        # Bottom row: left+1 to right
        for j in range(layer + 1, n - layer):
            ring.append(matrix[m - layer - 1][j])
        # Right column: bottom-1 to top+1
        for i in range(m - layer - 2, layer - 1, -1):
            ring.append(matrix[i][n - layer - 1])
        # Top row: right-1 to left+1
        for j in range(n - layer - 2, layer, -1):
            ring.append(matrix[layer][j])
        
        # Rotate right by r
        L = len(ring)
        rot = r % L
        if rot:
            ring = ring[-rot:] + ring[:-rot]
        
        # Put back
        idx = 0
        for i in range(layer, m - layer):
            matrix[i][layer] = ring[idx]
            idx += 1
        for j in range(layer + 1, n - layer):
            matrix[m - layer - 1][j] = ring[idx]
            idx += 1
        for i in range(m - layer - 2, layer - 1, -1):
            matrix[i][n - layer - 1] = ring[idx]
            idx += 1
        for j in range(n - layer - 2, layer, -1):
            matrix[layer][j] = ring[idx]
            idx += 1

    for row in matrix:
        print(*row)

matrix = [
    [1, 2, 3, 4],
    [12, 1, 2, 5],
    [11, 4, 3, 6],
    [10, 9, 8, 7]
]
r = 2

matrixRotation(matrix, r)
