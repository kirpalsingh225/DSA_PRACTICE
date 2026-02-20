class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = [0]
        r, c = len(grid), len(grid[0])

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    temp = [0]
                    self.dfs(i, j, grid, r, c, temp)

                    area[0] = max(area[0], temp[0])

        return area[0]

    def dfs(self, i, j, grid, r, c, temp):
        if i < 0 or i >= r or j < 0 or j >= c or grid[i][j] == 0:
            return

        temp[0]+=1
        grid[i][j] = 0
        self.dfs(i+1, j, grid, r, c, temp)
        self.dfs(i-1, j, grid, r, c, temp)
        self.dfs(i, j+1, grid, r, c, temp)
        self.dfs(i, j-1, grid, r, c, temp)