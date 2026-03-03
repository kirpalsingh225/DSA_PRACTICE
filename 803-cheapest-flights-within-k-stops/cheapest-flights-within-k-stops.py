from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf')]*n

        graph = {}
        for i in flights:
            a = i[0]
            b = i[1]
            d = i[2]

            if a not in graph:
                graph[a] = []

            graph[a].append((b, d))

        q = deque()

        q.append([src, 0])

        dist[src] = 0
        steps = 0

        while q and steps<=k:

            n = len(q)

            for i in range(n):
                node, d = q.popleft()

                for neighbor in graph.get(node, []):
                    nei = neighbor[0]
                    dis = neighbor[1]

                    if d + dis < dist[nei]:
                        dist[nei] = d+dis
                        q.append([nei, d+dis])


            steps+=1
                    
        if dist[dst]==float('inf'):
            return -1

        return dist[dst]