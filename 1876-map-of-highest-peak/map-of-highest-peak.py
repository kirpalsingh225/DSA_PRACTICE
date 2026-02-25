from collections import deque
from typing import List

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        
        r, c = len(isWater), len(isWater[0])
        height = [[-1] * c for _ in range(r)]
        q = deque()

        for i in range(r):
            for j in range(c):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                    q.append([i, j])

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while q:
            i, j = q.popleft()

            for di, dj in directions:
                i_ = i + di
                j_ = j + dj

                if i_ < 0 or i_ >= r or j_ < 0 or j_ >= c:
                    continue

                if height[i_][j_] != -1:
                    continue

                height[i_][j_] = height[i][j] + 1
                q.append([i_, j_])

        return height