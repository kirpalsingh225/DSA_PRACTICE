from collections import deque
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        target = (1 << n) - 1  # All bits set (all nodes visited)
        
        visited = set()
        q = deque()

        # Start from each node
        for i in range(n):
            q.append([i, 1 << i, 0])  # [node, mask, distance]
            visited.add((i, 1 << i))

        while q:
            node, mask, dist = q.popleft()  # Include distance

            # Check if all nodes visited
            if mask == target:  # Not just 1
                return dist

            for neighbor in graph[node]:
                next_mask = mask | (1 << neighbor)  # Set neighbor's bit

                if (neighbor, next_mask) not in visited:
                    visited.add((neighbor, next_mask))
                    q.append([neighbor, next_mask, dist + 1])

        return -1  # Should never reach here for valid input