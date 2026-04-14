class Solution:

    def dfs(self, graph, ch, visited):
        visited.add(ch)

        minchar = ch

        for c in graph[ch]:
            if c not in visited:
                minchar = min(minchar, self.dfs(graph, c, visited))


        return minchar



    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n = len(s1)

        m = len(baseStr)

        graph = defaultdict(list)

        for i in range(n):
            u = s1[i]
            v = s2[i]

            graph[u].append(v)
            graph[v].append(u)

        result = ""

        for i in range(m):
            ch = baseStr[i]
            visited = set()

            min_char = self.dfs(graph, ch, visited)

            result+=min_char

        return result