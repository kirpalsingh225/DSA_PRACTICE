from collections import deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        visited = set()

        q = deque()

        graph = {}

        for i in times:
            a = i[0]-1
            b = i[1]-1
            d = i[2]

            if a not in graph:
                graph[a] = []

            graph[a].append((b, d))

        dist = [float('inf')]*n
        dist[k-1] = 0

        q.append([k-1, 0])

        while q:
            node, dis = q.popleft()

            for n in graph.get(node, []):
                neighbor = n[0]
                d = n[1]

                if d + dis < dist[neighbor]:
                    dist[neighbor] = d + dis
                    q.append([neighbor, d+dis])

        ans = -1
        for i in dist:
            if i==float('inf'):
                return -1

            ans = max(ans, i)

        return ans

