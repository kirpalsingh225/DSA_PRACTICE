from collections import deque

class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:

        graph = {}

        for i in edges:
            a = i[0]
            b = i[1]

            if a not in graph:
                graph[a] = []
            graph[a].append(b)

            if b not in graph:
                graph[b] = []
            graph[b].append(a)

        
        result = float('inf')
        

        for i in range(n):  
            if i not in graph:  
                continue
                
            visited = {i: 0}  
            q = deque()
            q.append([i, -1])  

            while q:
                node, parent = q.popleft()

                for neighbor in graph.get(node, []):
                    if neighbor not in visited:
                        visited[neighbor] = visited[node] + 1 
                        q.append([neighbor, node])
                        
                    elif neighbor != parent:
                        
                        cycle_length = visited[node] + visited[neighbor] + 1
                        result = min(result, cycle_length)


        if result == float('inf'):
            return -1

        return result