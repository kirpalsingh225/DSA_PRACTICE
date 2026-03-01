from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        r, c = len(grid), len(grid[0])


        q = deque()
        visited = set()
        found = False
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    self.dfs(i, j, grid, r, c, visited)
                    found = True
                    break
            if found:
                break

        for i in visited:
            q.append(i)

        level = 0
        directionx = [1, 0, -1, 0]
        directiony = [0, 1, 0, -1]
        while q:
            n = len(q)

            for i in range(n):
                x, y = q.popleft()

                # if grid[x][y] == 1:
                #     return level

                for j in range(4):
                    new_x = x + directionx[j]
                    new_y = y + directiony[j]

                    if new_x<0 or new_x>=r or new_y<0 or new_y>=c:
                        continue

                    if (new_x, new_y) not in visited:
                        if grid[new_x][new_y] == 1:  # check neighbor instead
                            return level
                        visited.add((new_x, new_y))
                        q.append((new_x, new_y))

            level+=1


    
    def dfs(self, i, j, grid, r, c, visited):
        if i < 0 or i >= r or j < 0 or j>= c or grid[i][j]==0 or (i, j) in visited:
            return

        visited.add((i, j))
        self.dfs(i+1, j, grid, r,c,  visited)
        self.dfs(i-1, j, grid, r,c ,visited)
        self.dfs(i, j+1, grid, r,c ,visited)
        self.dfs(i, j-1, grid, r,c ,visited)