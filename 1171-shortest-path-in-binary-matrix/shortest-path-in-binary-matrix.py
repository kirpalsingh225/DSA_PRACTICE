from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])

        if m==0 or n==0 or grid[0][0]!=0:
            return -1


        q = deque()

        q.append([0, 0])
        grid[0][0] = 1

        level = 0

        directions = [(1, 1), (0, 1), (1, 0), (-1,0), (0, -1), (-1,-1), (1, -1), (-1, 1)] 
        while q:
            l = len(q)

            for i in range(l):
                x, y = q.popleft()

                if x == m-1 and y == n-1:
                    return level+1

                for dirs in directions:
                    new_x = x+dirs[0]
                    new_y = y+dirs[1]

                    if new_x<0 or new_x>=m or new_y< 0 or new_y>=n or grid[new_x][new_y]==1:
                        continue


                    q.append([new_x, new_y])
                    grid[new_x][new_y] = 1

            level+=1


        return -1

 


