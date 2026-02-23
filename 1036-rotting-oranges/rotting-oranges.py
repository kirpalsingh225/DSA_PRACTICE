from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        level = 0
        q = deque()

        visited = set()

        r, c = len(grid), len(grid[0])
        


        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    q.append([i, j])
                    visited.add((i, j))

        while q:
            n = len(q)

            for i in range(n):
                cur_x, cur_y = q.popleft()

                directions_x = [1, 0, -1, 0]
                directions_y = [0, 1, 0, -1]

                # neighbors
                for k in range(4):
                    next_x = cur_x + directions_x[k]
                    next_y = cur_y + directions_y[k]

                    if next_x < 0 or next_x >= r or next_y < 0 or next_y >= c or grid[next_x][next_y]==0:
                        continue

                    if (next_x, next_y) not in visited:
                        grid[next_x][next_y] = 2
                        visited.add((next_x, next_y))
                        q.append([next_x, next_y])


            level+=1

        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    return -1

        if level==0:
            return level
        return level-1
