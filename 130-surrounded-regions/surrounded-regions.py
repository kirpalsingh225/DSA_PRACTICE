class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        r, c = len(grid), len(grid[0])

        for j in range(c):
            if grid[0][j] == 'O':
                self.dfs(0, j, grid, r, c)
            if grid[r-1][j] == 'O':
                self.dfs(r-1, j, grid, r, c)

        for i in range(r):
            if grid[i][0] == 'O':
                self.dfs(i, 0, grid, r, c)
            if grid[i][c-1] == 'O':
                self.dfs(i, c-1, grid, r, c)

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 'O':
                    grid[i][j] = 'X'
                elif grid[i][j] == 'm':
                    grid[i][j] = 'O'

    def dfs(self, i, j, grid, r, c):
        if i < 0 or i >= r or j < 0 or j >= c or grid[i][j] != 'O':
            return
        grid[i][j] = 'm'
        self.dfs(i+1, j, grid, r, c)
        self.dfs(i-1, j, grid, r, c)
        self.dfs(i, j+1, grid, r, c)
        self.dfs(i, j-1, grid, r, c)