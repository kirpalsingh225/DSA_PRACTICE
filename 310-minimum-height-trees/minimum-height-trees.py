from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        result = []
        indegree = [0]*n

        graph = {} 
        for i in edges:
            a = i[0]
            b = i[1]

            indegree[a] +=1
            indegree[b] +=1
            if a not in graph:
                graph[a] = []

            graph[a].append(b)

            if b not in graph:
                graph[b] = []
            graph[b].append(a)

        q = deque()

        for i in range(n):
            if indegree[i] == 1:
                q.append(i)

        while n > 2:
            size = len(q)

            n-=size

            for i in range(size):
                u = q.popleft()

                for v in graph.get(u, []):
                    indegree[v]-=1
                    if indegree[v]==1:
                        q.append(v)


        while q:
            result.append(q.popleft())

        return result

        

