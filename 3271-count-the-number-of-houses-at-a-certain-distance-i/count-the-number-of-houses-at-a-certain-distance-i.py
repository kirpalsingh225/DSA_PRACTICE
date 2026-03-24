from collections import deque
from typing import List

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        
        graph = {i: [] for i in range(1, n+1)}

        # line connections
        for i in range(1, n):
            graph[i].append(i+1)
            graph[i+1].append(i)

        # extra connection
        graph[x].append(y)
        graph[y].append(x)

        ans = [0]*(n+1)

        # BFS from each node
        for i in range(1, n+1):
            q = deque()
            visited = set()
            q.append((i, 0))
            visited.add(i)

            while q:
                curr, dist = q.popleft()

                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append((neighbor, dist+1))
                        ans[dist+1] += 1

        return ans[1:]