from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        r, c = len(mat), len(mat[0])
        result = [[-1] * c for _ in range(r)]
        q = deque()

        # Add all 0 cells as sources
        for i in range(r):
            for j in range(c):
                if mat[i][j] == 0:
                    result[i][j] = 0
                    q.append((i, j))

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while q:
            x, y = q.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if nx < 0 or nx >= r or ny < 0 or ny >= c:
                    continue

                if result[nx][ny] != -1:  # already visited
                    continue

                result[nx][ny] = result[x][y] + 1
                q.append((nx, ny))

        return result