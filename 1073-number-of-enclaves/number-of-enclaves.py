from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        result = 0

        for j in range(c):
            if grid[0][j] == 1:
                self.dfs(0, j, grid, r, c)

        # 2️⃣ Bottom row
        for j in range(c):
            if grid[r-1][j] == 1:
                self.dfs(r-1, j, grid, r, c)

        # 3️⃣ Left column
        for i in range(r):
            if grid[i][0] == 1:
                self.dfs(i, 0, grid, r, c)

        # 4️⃣ Right column
        for i in range(r):
            if grid[i][c-1] == 1:
                self.dfs(i, c-1, grid, r, c)

        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    result+=1

        return result


    def dfs(self, i, j, grid, r, c):
        if i < 0 or i>=r or j < 0 or j>=c or grid[i][j]==0:
            return

        grid[i][j] = 0

        self.dfs(i+1, j , grid, r, c)
        self.dfs(i-1, j , grid, r, c)
        self.dfs(i, j+1 , grid, r, c)
        self.dfs(i, j-1 , grid, r, c)


            
