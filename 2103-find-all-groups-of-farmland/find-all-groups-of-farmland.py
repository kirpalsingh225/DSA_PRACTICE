class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        r, c = len(land), len(land[0])
        result = []

        for i in range(r):
            for j in range(c):
                if land[i][j] == 1:
                    bottom_r, bottom_c = self.dfs(i, j, land, r, c)
                    result.append([i, j, bottom_r, bottom_c])

        return result

    def dfs(self, i, j, land, r, c):
        if i < 0 or i >= r or j < 0 or j >= c or land[i][j] == 0:
            return -1, -1   # important!

        land[i][j] = 0

        max_row, max_col = i, j

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        for dx, dy in directions:
            x, y = self.dfs(i + dx, j + dy, land, r, c)
            max_row = max(max_row, x)
            max_col = max(max_col, y)

        return max_row, max_col