class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = {}

        n = len(quiet)
        ans = [-1]*n

        for i in richer:
            a = i[0]
            b = i[1]

            if b not in graph:
                graph[b] = []

            graph[b].append(a)

        for i in range(n):
            ans[i] = self.dfs(i, ans, graph, quiet)

        return ans

    def dfs(self, node, ans, graph, quiet):
        if ans[node] != -1:
            return ans[node]

        minPos = node
        minQ = quiet[node]

        for neighbor in graph.get(node, []):
            ind = self.dfs(neighbor, ans, graph, quiet)
            if minQ > quiet[ind]:
                minQ = quiet[ind]
                minPos = ind

        ans[node] = minPos
        return minPos