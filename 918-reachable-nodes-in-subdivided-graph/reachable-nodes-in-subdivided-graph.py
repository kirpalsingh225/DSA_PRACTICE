from collections import deque

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = {}

        for i in edges:
            a = i[0]
            b = i[1]
            d = i[2]

            if a not in graph:
                graph[a] = []

            graph[a].append((b, d+1))

            if b not in graph:
                graph[b] = []

            graph[b].append((a, d+1))

        q = deque()
        q.append([0, 0])
        dist = [float('inf')]*n
        dist[0] = 0
        while q:
            node, distance = q.popleft()

            if distance > dist[node]:
                continue

            for neighbor in graph.get(node, []):
                nei = neighbor[0]
                nei_d = neighbor[1]

                if distance + nei_d < dist[nei]:
                    dist[nei] = distance + nei_d 
                    q.append((nei, dist[nei]))


        ans = 0
        for i in range(n):
            if dist[i] <= maxMoves:
                ans+=1

        for u, v, cnt in edges:
            moves_u = max(0, maxMoves - dist[u])
            moves_v = max(0, maxMoves - dist[v])

            reachable = min(cnt, moves_u + moves_v)
            ans += reachable

        return ans