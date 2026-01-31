from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {}
        indegree = [0]*numCourses

        for i in prerequisites:
            a = i[0]
            b = i[1]

            # b --> a

            if b not in graph:
                graph[b] = []

            graph[b].append(a)
            indegree[a]+=1

        q = deque()
        count = 0
        for i, degree in enumerate(indegree):
            if degree == 0:
                count += 1
                q.append(i)

        
        while q:
            curr = q.popleft()

            for n in graph.get(curr, []):
                indegree[n]-=1

                if indegree[n] == 0:
                    count+=1
                    q.append(n)

        if count == numCourses:
            return True
        return False
        