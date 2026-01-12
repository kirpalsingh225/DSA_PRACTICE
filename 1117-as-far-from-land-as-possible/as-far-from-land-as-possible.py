from collections import deque
from typing import List

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Multi-source BFS: Start from ALL land cells at once
        q = deque()
        visited = set()
        
        # Add all land cells to queue
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j, 0))  # (row, col, distance)
                    visited.add((i, j))
        
        # Edge cases
        if len(q) == 0 or len(q) == n * n:
            return -1  # No land or no water
        
        max_distance = -1
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while q:
            x, y, dist = q.popleft()
            
            # Explore all 4 directions
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # Check bounds and if not visited
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    q.append((nx, ny, dist + 1))
                    max_distance = max(max_distance, dist + 1)
        
        return max_distance