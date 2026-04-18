from typing import List
from collections import defaultdict

class Solution:

    def dfs(self, graph, src, dst, visited, product):
        if src == dst:
            return product

        visited.add(src)

        for nei, val in graph.get(src, []):
            if nei not in visited:
                res = self.dfs(graph, nei, dst, visited, product * val)
                if res != -1:
                    return res

        return -1.0

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(list)

        # build graph
        for (u, v), val in zip(equations, values):
            graph[u].append((v, val))
            graph[v].append((u, 1 / val))

        result = []

        for src, dst in queries:
            if src not in graph or dst not in graph:
                result.append(-1.0)
            else:
                visited = set()
                ans = self.dfs(graph, src, dst, visited, 1.0)
                result.append(ans)

        return result