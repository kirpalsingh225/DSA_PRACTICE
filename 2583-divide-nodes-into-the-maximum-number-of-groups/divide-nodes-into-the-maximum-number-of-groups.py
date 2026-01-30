from collections import deque

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph = {}

        for i in edges:
            a = i[0] - 1
            b = i[1] - 1

            if a not in graph:
                graph[a] = []
            graph[a].append(b)

            if b not in graph:
                graph[b] = []
            graph[b].append(a)

        colors = [-1] * n
        for i in range(n):
            if colors[i] == -1:
                if not self.isBipartite(graph, i, colors, 1):
                    return -1

        levels = [0] * n
        for i in range(n):
            levels[i] = self.bfs(graph, i, n)

        maxGps = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                maxGps += self.getMax(graph, i, visited, levels)

        return maxGps

    def isBipartite(self, graph, curr, colors, currColor):
        colors[curr] = currColor

        for n in graph.get(curr, []):
            if colors[n] == colors[curr]:
                return False
            
            if colors[n] == -1:
                if not self.isBipartite(graph, n, colors, 1 - currColor):
                    return False

        return True

    def bfs(self, graph, curr, n):
        q = deque()
        visited = set()

        q.append(curr)
        visited.add(curr)

        level = 0

        while q:
            sze = len(q)

            for i in range(sze):
                curr_node = q.popleft()
                
                for neighbor in graph.get(curr_node, []):
                    if neighbor in visited:
                        continue
                    q.append(neighbor)
                    visited.add(neighbor)

            level += 1

        return level

    def getMax(self, graph, curr, visited, levels):
        maxGp = levels[curr]
        visited.add(curr)

        for n in graph.get(curr, []):
            if n not in visited:
                maxGp = max(maxGp, self.getMax(graph, n, visited, levels))
        
        return maxGp