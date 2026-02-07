class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])

        dp = {} # (r, c)

        def dfs(r, c, prevVal):
            if r <0 or r == row or c <0 or c==col or matrix[r][c]<=prevVal:
                return 0

            if (r, c) in dp:
                return dp[(r, c)]

            res = 1

            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))

            res = max(res, 1 + dfs(r , c+1, matrix[r][c]))

            res = max(res, 1 + dfs(r , c-1, matrix[r][c]))
            dp[(r, c)] = res
            return res

        for r in range(row):
            for c in range(col):
                dfs(r, c, -1)


        return max(dp.values())

