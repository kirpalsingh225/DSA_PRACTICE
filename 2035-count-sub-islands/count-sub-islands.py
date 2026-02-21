class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        r, c = len(grid1), len(grid1[0])
        subislands = 0

        for i in range(r):
            for j in range(c):
                if grid2[i][j] == 1:
                    if self.checkSubIsland(grid1, grid2, i, j, r, c):
                        subislands += 1

        return subislands

    def checkSubIsland(self, grid1, grid2, i, j, r, c):
        if i < 0 or i >= r or j < 0 or j >= c:
            return True
        if grid2[i][j] != 1:
            return True
        
        grid2[i][j] = -1  # mark visited
        
        result = (grid1[i][j] == 1)
        
        top    = self.checkSubIsland(grid1, grid2, i+1, j, r, c)
        bottom = self.checkSubIsland(grid1, grid2, i-1, j, r, c)
        right  = self.checkSubIsland(grid1, grid2, i, j+1, r, c)
        left   = self.checkSubIsland(grid1, grid2, i, j-1, r, c)
    
        return result and top and bottom and right and left