from collections import deque

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = {}

        for i in dislikes:
            a = i[0]
            b = i[1]

            if a not in graph:
                graph[a] = []
            graph[a].append(b)

            if b not in graph:
                graph[b] = []
            graph[b].append(a)

        color = [-1] * (n + 1)

        for i in range(1, n + 1):  
            if color[i] == -1: 
                q = deque()
                q.append(i)
                color[i] = 1

                while q:
                    curr = q.popleft()

                    for neighbor in graph.get(curr, []):  
                        if color[curr] == color[neighbor]:
                            return False

                        if color[neighbor] == -1:
                            q.append(neighbor)
                            color[neighbor] = 1 - color[curr]

        return True