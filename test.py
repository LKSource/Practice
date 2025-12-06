def knightlOnAChessboard(n):
    # Write your code here
    arr = []
    for i in range(1, n):
        results = []
        for j in range(1, n):
            r = []
            #print(f"({i},{j})", end=" ")
            # Implement BFS or DFS to find the shortest path
            from collections import deque
            visited = [[False]*n for _ in range(n)]
            queue = deque()
            queue.append((0, 0, 0))  # (x, y,
            visited[0][0] = True
            found = False
            while queue:
                x, y, dist = queue.popleft()
                if x == n-1 and y == n-1:
                    r.append(dist)
                    found = True
                    break
                for dx, dy in [(i, j), (i, -j), (-i, j), (-i, -j), (j, i), (j, -i), (-j, i), (-j, -i)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny, dist + 1))
            if found:
                #print(r[0], end=" ")
                results.append(r[0])
            else:
                #print(-1, end=" ")  
                results.append(-1)
        #print(results)
        arr.append(results)    
        #print()
    return arr

print(knightlOnAChessboard(5))
