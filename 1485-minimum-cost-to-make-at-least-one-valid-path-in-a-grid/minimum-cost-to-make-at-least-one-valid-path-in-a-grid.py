from collections import deque
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        q = deque()
        q.append([0, 0, 0])
        result = [[float('inf')] * n for _ in range(m)]
        result[0][0] = 0

        while q:
            currCost, i, j = q.popleft()

            if currCost > result[i][j]:
                continue

            for k in range(4):
                i_ = i + dirs[k][0]
                j_ = j + dirs[k][1]

                if i_ >= 0 and j_ >= 0 and i_ < m and j_ < n:
                    dirCost = 0 if grid[i][j]-1 == k else 1
                    newCost = currCost + dirCost

                    if newCost < result[i_][j_]:
                        result[i_][j_] = newCost
                        if dirCost == 0:
                            q.appendleft([newCost, i_, j_])
                        else:
                            q.append([newCost, i_, j_])

        return result[m-1][n-1]