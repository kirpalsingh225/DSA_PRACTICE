from collections import deque

class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        fireGrid = [[float("inf")] * col for _ in range(row)]

        self.updateFireTime(fireGrid, grid)  # Added self.

        ans = -1
        left = 0
        right = row * col + 1  # Fixed: was m*n+1

        while left <= right:
            mid = (left + right) // 2

            if self.isPossible(mid, fireGrid):  # Added self.
                left = mid + 1
                ans = mid
            else:
                right = mid - 1

        return 10**9 if ans == row * col + 1 else ans

    def updateFireTime(self, fireGrid, grid):
        row = len(grid)
        col = len(grid[0])

        visited = set()
        q = deque()
        currtime = 0

        # Find all initial fire positions
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    visited.add((i, j))  # Fixed: was (x, y)
                    fireGrid[i][j] = currtime
                    q.append([i, j])
                elif grid[i][j] == 2:
                    fireGrid[i][j] = -1

        # Directions
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        while q:
            currtime += 1
            n = len(q)

            for _ in range(n):  # Changed i to _
                x, y = q.popleft()

                for j in range(4):
                    nx = x + dx[j]  # Fixed: was dx[j] before defining
                    ny = y + dy[j]  # Fixed: was dy[j]

                    if nx < 0 or ny < 0 or ny >= col or nx >= row or fireGrid[nx][ny] == -1 or (nx, ny) in visited:
                        continue

                    fireGrid[nx][ny] = currtime
                    visited.add((nx, ny))
                    q.append([nx, ny])

    def isPossible(self, mid, fireGrid):  # Added self
        row = len(fireGrid)
        col = len(fireGrid[0])

        visited = set()
        q = deque()

        currtime = mid  # Fixed typo: was 'curtime' in some places

        if fireGrid[0][0] <= currtime:
            return False

        q.append([0, 0])
        visited.add((0, 0))

        # Directions
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        while q:
            currtime += 1  # Fixed typo: was 'curtime'
            n = len(q)

            for _ in range(n):  # Changed i to _
                x, y = q.popleft()

                for j in range(4):
                    nx = x + dx[j]
                    ny = y + dy[j]

                    if nx < 0 or ny < 0 or ny >= col or nx >= row or fireGrid[nx][ny] == -1 or (nx, ny) in visited:
                        continue

                    # Check if reached destination
                    if nx == row - 1 and ny == col - 1 and currtime <= fireGrid[row - 1][col - 1]:
                        return True

                    # Can move if we arrive before fire
                    if currtime < fireGrid[nx][ny]:
                        visited.add((nx, ny))
                        q.append([nx, ny])

        return False  # Added missing return