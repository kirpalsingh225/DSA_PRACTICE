from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []

        indegree = [0]*numCourses
        graph = {}

        for i in prerequisites:
            a = i[0]
            b = i[1]

            # b -> a
            if b not in graph:
                graph[b] = []

            graph[b].append(a)

            indegree[a]+=1

        count = 0
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                result.append(i)
                count+=1
                q.append(i)

        
        while q:
            curr = q.popleft()
            
            for n in graph.get(curr, []):
                indegree[n]-=1

                if indegree[n] == 0:
                    result.append(n)
                    count+=1
                    q.append(n)


        if count==numCourses:
            return result
        return []
