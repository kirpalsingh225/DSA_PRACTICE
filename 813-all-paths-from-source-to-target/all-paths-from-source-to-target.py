class Solution:

    def dfs(self, graph, src, target, result, temp):
        temp.append(src)

        if src == target:
            result.append(temp[:])

        for n in graph[src]:
            self.dfs(graph, n, target, result, temp)

        temp.pop()

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        temp = []


        self.dfs(graph, 0, len(graph)-1, result, temp)

        return result
