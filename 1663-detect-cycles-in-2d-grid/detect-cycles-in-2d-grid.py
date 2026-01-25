from collections import deque
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        
        visited = set()
        
        row = len(grid)
        col = len(grid[0])

        x = [0, 1, -1, 0]
        y = [1, 0, 0, -1]

        for i in range(row):
            for j in range(col):

                if (i, j) not in visited:

                    q = deque()
                    q.append([i, j, -1, -1])
                    visited.add((i, j))

                    while q:
                        X, Y, parentx, parenty = q.popleft()

                        for k in range(4):  # ← Changed from 'i' to 'k'
                            nx = X + x[k]
                            ny = Y + y[k]

                            if nx < 0 or nx >= row or ny < 0 or ny >= col or grid[nx][ny] != grid[X][Y]:
                                continue

                            if nx == parentx and ny == parenty:
                                continue

                            if (nx, ny) in visited:
                                return True

                            visited.add((nx, ny))
                            q.append([nx, ny, X, Y])

        return False