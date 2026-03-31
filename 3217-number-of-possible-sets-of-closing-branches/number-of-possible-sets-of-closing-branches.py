from typing import List

class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        result = 0 

        for mask in range(1 << n):  # iterate all subsets
            
            # adjacency matrix
            grid = [[float('inf')] * n for _ in range(n)]

            # build graph for selected nodes
            for u, v, w in roads:
                if (mask >> u) & 1 and (mask >> v) & 1:
                    grid[u][v] = min(grid[u][v], w)
                    grid[v][u] = min(grid[v][u], w)

            # distance to self = 0
            for i in range(n):
                grid[i][i] = 0

            # Floyd-Warshall
            for via in range(n):
                for i in range(n):
                    for j in range(n):
                        if grid[i][via] != float('inf') and grid[via][j] != float('inf'):
                            grid[i][j] = min(grid[i][j], grid[i][via] + grid[via][j])

            # check condition
            ok = True
            for i in range(n):
                for j in range(n):
                    if i != j and ((mask >> i) & 1) and ((mask >> j) & 1):
                        if grid[i][j] > maxDistance:
                            ok = False
                            break
                if not ok:
                    break

            if ok:
                result += 1

        return result