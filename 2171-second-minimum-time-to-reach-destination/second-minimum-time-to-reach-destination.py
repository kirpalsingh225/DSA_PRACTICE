from collections import deque
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = {}
        for edge in edges:
            a = edge[0]
            b = edge[1]

            if a not in graph: graph[a] = []
            if b not in graph: graph[b] = []
            graph[a].append(b)
            graph[b].append(a)

        d1 = [float('inf')] * (n+1)
        d2 = [float('inf')] * (n+1)

        q = deque()
        q.append([0, 1])
        d1[1] = 0

        while q:
            timePassed, node = q.popleft()

            if node == n and d2[n] != float('inf'):
                return d2[n]

            div = timePassed // change
            if div % 2 == 1:  # red light
                timePassed = change * (div + 1)

            for neighbor in graph.get(node, []):
                if d1[neighbor] > timePassed + time:
                    d2[neighbor] = d1[neighbor]
                    d1[neighbor] = timePassed + time
                    q.append([timePassed + time, neighbor])

                elif d2[neighbor] > timePassed + time and d1[neighbor] != timePassed + time:
                    d2[neighbor] = timePassed + time
                    q.append([timePassed + time, neighbor])

        return d2[n]