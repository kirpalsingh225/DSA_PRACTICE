from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = {}

        

        for i in range(len(graph)):
            if i not in visited:
                q = deque()
                visited[i] = 'r'
                q.append([i, 'r'])

            while q:
                curr_node, color = q.popleft()

                for neighbor in graph[curr_node]:
                    if neighbor not in visited:
                        if color == 'b':
                            visited[neighbor] = 'r'
                            q.append([neighbor, 'r'])
                        else:
                            visited[neighbor] = 'b'
                            q.append([neighbor, 'b'])
                        
                    elif visited[neighbor] == color:
                        return False


        return True
                    

                
