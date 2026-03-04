from collections import deque
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        graph = {}

        for i in range(len(edges)):
            a = edges[i][0]
            b = edges[i][1]
            prob = succProb[i]

            if a not in graph:
                graph[a] = []

            graph[a].append((b, prob))

            if b not in graph:
                graph[b] = []

            graph[b].append((a, prob))

        q = deque()

        dist = [float('-inf')]*n
        dist[start_node] = 1

        q.append([start_node, 1])

        while q:
            n = len(q)


            for i in range(n):
                node, node_d = q.popleft()

                for neighbor in graph.get(node, []):
                    nei = neighbor[0]
                    nei_d = neighbor[1]

                    if node_d * nei_d > dist[nei]:
                        dist[nei] = node_d * nei_d
                        q.append([nei, dist[nei]])

        
        if dist[end_node] == float('-inf'):
            return 0

        return dist[end_node]