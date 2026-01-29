from collections import deque

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = {}
        
        for i in paths:
            a = i[0]
            b = i[1]
            
            if a not in graph:
                graph[a] = []
            graph[a].append(b)
            
            if b not in graph:
                graph[b] = []
            graph[b].append(a)
        
        answer = [0] * (n + 1)
        
        for i in range(1, n + 1):
            if answer[i] == 0:
                q = deque()
                q.append(i)
                answer[i] = 1
                
                while q:
                    level_size = len(q)  # Process level by level
                    
                    for _ in range(level_size):
                        curr = q.popleft()
                        
                        for neighbor in graph.get(curr, []):
                            if answer[neighbor] == 0:
                                # Find colors used by neighbor's neighbors
                                used_colors = set()
                                for adj in graph.get(neighbor, []):
                                    if answer[adj] != 0:
                                        used_colors.add(answer[adj])
                                
                                # Pick first available color
                                for color in [1, 2, 3, 4]:
                                    if color not in used_colors:
                                        answer[neighbor] = color
                                        break
                                
                                q.append(neighbor)
        
        return answer[1:]