from collections import deque

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        l = 0
        r = len(cells) - 1
        result = 0

        while l <= r:
            mid = (l + r) // 2

            if self.canCross(cells, mid, row, col):
                result = mid + 1
                l = mid + 1
            else:
                r = mid - 1

        return result

    def canCross(self, cells, day, row, col):
        # Create grid with water up to 'day'
        grid = [[0] * col for _ in range(row)]
        
        for i in range(day + 1):
            x = cells[i][0] - 1
            y = cells[i][1] - 1
            grid[x][y] = 1
        
        # BFS from all starting positions in first row
        q = deque()
        visited = [[False] * col for _ in range(row)]  # Use 2D array instead of set
        
        # Add all valid starting positions
        for j in range(col):
            if grid[0][j] == 0:
                q.append((0, j))
                visited[0][j] = True
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while q:
            i, j = q.popleft()
            
            # Reached last row
            if i == row - 1:
                return True
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                
                if 0 <= ni < row and 0 <= nj < col and grid[ni][nj] == 0 and not visited[ni][nj]:
                    visited[ni][nj] = True
                    q.append((ni, nj))
        
        return False