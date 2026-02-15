from collections import deque
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        
        graph = {}
        indegree = [0]*n

        for i in range(len(relations)):
            u = relations[i][0] -1
            v = relations[i][1]-1
            
            if u not in graph:
                graph[u] = []

            graph[u].append(v)
            indegree[v]+=1

        q = deque()
        maxtime = [0]*n

        for i in range(n):
            if indegree[i]==0:
                q.append(i)
                maxtime[i] = time[i]


        while q:
            u = q.popleft()

            for neighbor in graph.get(u, []):
                maxtime[neighbor] = max(maxtime[neighbor], maxtime[u] + time[neighbor])
                indegree[neighbor]-=1
                if indegree[neighbor] == 0:
                    q.append(neighbor)


        
        return max(maxtime)
