from collections import deque
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph = {}

        for x in prerequisites:
            u = x[0]
            v = x[1]

            if u not in graph:
                graph[u] = []

            graph[u].append(v)

        q_size = len(queries)
        ans = [False]*q_size

        for i in range(q_size):
            u = queries[i][0]
            v = queries[i][1]

            visited = set()
            ans[i] = self.dfs(graph, u, v, visited)

        return ans


    def dfs(self, graph, src, dest, visited):

        visited.add(src)

        if src==dest:
            return True

        isReachable = False
        for neighbor in graph.get(src, []):
            if neighbor not in visited:
                isReachable = isReachable or self.dfs(graph, neighbor, dest, visited)

        return isReachable
