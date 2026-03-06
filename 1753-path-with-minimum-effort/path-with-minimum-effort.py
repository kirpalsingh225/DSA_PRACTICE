from collections import deque
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        r, c = len(heights), len(heights[0])

        result = [[float('inf')]*c for _ in range(r)]

        q = deque()

        q.append([[0, 0], 0])  # fix 1: single argument
        result[0][0] = 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            coord, diff = q.popleft()

            x = coord[0]
            y = coord[1]

            if diff > result[x][y]:  
                continue

            for i in directions:
                x_ = x + i[0]
                y_ = y + i[1]

                if x_ < 0 or x_>=r or y_<0 or y_>=c:
                    continue

                abs_diff = abs(heights[x][y] - heights[x_][y_])
                max_diff = max(diff, abs_diff)  

                if result[x_][y_] > max_diff:
                    result[x_][y_] = max_diff
                    q.append([[x_, y_], max_diff])

        return result[r-1][c-1]