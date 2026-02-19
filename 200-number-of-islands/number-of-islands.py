class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        r, c = len(grid), len(grid[0])

        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    islands+=1
                    self.dfs(i, j, grid, r, c)

        return islands
                    

    def dfs(self, i, j, grid, r, c):
        if i < 0 or i >= r or j < 0 or j >= c or grid[i][j] == '0':
            return

        grid[i][j] = '0'
        self.dfs(i+1, j, grid, r, c) 
        self.dfs(i-1, j, grid, r, c) 
        self.dfs(i, j+1, grid, r, c) 
        self.dfs(i, j-1, grid, r, c) 


    

        

        