from collections import deque

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # solution
        degree = [0]*n
        graph = {}

        for a, b in edges:
            
            if a not in graph:
                graph[a] = []
            degree[a]+=1
            graph[a].append(b)
            
            
            if b not in graph:
                graph[b] = []
            degree[b]+=1
            graph[b].append(a)
        
        
        visited = set()
        complete_components = 0

        for i in range(n):
            curr_visited = set()
            if i not in visited:
                visited.add(i)
                
                
                q = deque()
                q.append(i)

                while q:
                    curr_node = q.popleft()

                    curr_visited.add(curr_node)

                    for neighbor in graph.get(curr_node, [float('inf')]):
                        if neighbor == float('inf'):
                            continue
                        elif neighbor not in visited:
                            q.append(neighbor)
                            visited.add(neighbor)
                        
                result = self.checkComplete(curr_visited, degree)
                if result:
                    complete_components+=1

        return complete_components


    def checkComplete(self, curr_visited, degree):
        for i in curr_visited:
            if degree[i] != len(curr_visited)-1:
                return False

        return True







        
