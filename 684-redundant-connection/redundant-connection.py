from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        graph = {}

        for u, v in edges:
            visited = set()

            # check if path already exists
            if u in graph and v in graph and self.dfs(graph, u, v, visited):
                return [u, v]

            # build graph
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []

            graph[u].append(v)
            graph[v].append(u)

    def dfs(self, adj, u, target, visited):
        if u == target:
            return True

        visited.add(u)

        for neighbor in adj.get(u, []):
            if neighbor not in visited:
                if self.dfs(adj, neighbor, target, visited):
                    return True

        return False