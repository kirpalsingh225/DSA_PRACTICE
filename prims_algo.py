import heapq
from collections import defaultdict
from typing import List

class Solution:
    def prims(self, n: int, edges: List[List[int]]) -> int:
        # build graph
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        visited = set()
        min_heap = [(0, 0)]  # (weight, node)
        total_cost = 0

        while min_heap and len(visited) < n:
            weight, node = heapq.heappop(min_heap)

            if node in visited:
                continue

            visited.add(node)
            total_cost += weight

            for nei, w in graph[node]:
                if nei not in visited:
                    heapq.heappush(min_heap, (w, nei))

        # if not all nodes visited → graph not connected
        return total_cost if len(visited) == n else -1
