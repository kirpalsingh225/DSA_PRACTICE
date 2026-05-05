class Solution:

    def dfs(self, i, visited, graph):
        visited.add(i)

        for n in graph.get(i, []):
            if n not in visited:
                self.dfs(n, visited, graph)

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)

        graph = defaultdict(list)

        for i in range(n):
            for j in range(n):
                if i==j:
                    continue

                x1 = bombs[i][0]
                y1 = bombs[i][1]
                r1 = bombs[i][2]

                x2 = bombs[j][0]
                y2 = bombs[j][1]
                r2 = bombs[j ][2]

                d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

                if r1 >= d:
                    graph[i].append(j)


        result = 0
        
        for i in range(n):
            visited = set()
            self.dfs(i, visited, graph)

            count = len(visited)
            result = max(count, result)


        return result
