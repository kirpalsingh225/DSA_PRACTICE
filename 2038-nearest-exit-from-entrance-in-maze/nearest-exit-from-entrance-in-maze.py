from collections import deque
from typing import List
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        r, c = len(maze), len(maze[0])
        q = deque()

        q.append([entrance[0], entrance[1], 0])
        maze[entrance[0]][entrance[1]] = '+'

        direction_x = [0, 1, -1 , 0]
        direction_y = [1, 0, 0, -1]

        ans = float('inf')

        while q:
            x, y, distance = q.popleft()

            for i in range(4):
                new_x = x + direction_x[i]
                new_y = y + direction_y[i]

                if new_x<0 or new_x>=r or new_y<0 or new_y>=c or maze[new_x][new_y]=='+':
                    continue

                if new_x == 0 or new_x == r-1 or new_y == 0 or new_y == c-1:
                    ans = min(ans, distance+1)
                    # q.append([new_x, new_y, distance+1])
                maze[new_x][new_y] = '+'
                q.append([new_x, new_y, distance+1])

        if ans == float('inf'):
            return -1
        return ans