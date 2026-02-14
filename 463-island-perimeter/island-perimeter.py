class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        r, c = len(grid), len(grid[0])
        ans = [0]

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    self.dfs(i, j, grid, ans, r, c)
                    


        return ans[0]


    def dfs(self, i, j, grid, perimeter, r, c):
        
        if i < 0 or i >= r or j < 0 or j >= c or grid[i][j]==0:
            perimeter[0]+=1
            return

        if grid[i][j] == -1:  # Already visited
            return

        grid[i][j] = -1
        self.dfs(i+1, j, grid, perimeter, r, c)
        self.dfs(i-1, j , grid, perimeter, r, c)
        self.dfs(i, j+1, grid, perimeter, r, c)
        self.dfs(i, j-1, grid, perimeter, r, c)