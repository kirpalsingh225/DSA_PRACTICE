class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = [False] * len(graph)
        inRecur = [False] * len(graph)

        safe_nodes = []
        for i in range(len(graph)):
            if not visited[i]:
                self.isCycleDFS(graph, i, visited, inRecur)
                
        for i in range(len(graph)):
            if inRecur[i] == False:
                safe_nodes.append(i)
        return safe_nodes

    def isCycleDFS(self, graph, u, visited, inRecur):
        visited[u] = True
        inRecur[u] = True

        for n in graph[u]:
            if not visited[n] and self.isCycleDFS(graph, n, visited, inRecur):
                return True
            elif inRecur[n] == True:
                return True

        inRecur[u] = False
        return False