import heapq

def dijkstra(graph, n):

    dist = [float('inf')] * n
    dist[0] = 0

    pq = []
    heapq.heappush(pq, (0, 0))  # (distance, node)

    while pq:
        distance, node = heapq.heappop(pq)

        if distance > dist[node]:
            continue

        for nei, w in graph.get(node, []):
            if distance + w < dist[nei]:
                dist[nei] = distance + w
                heapq.heappush(pq, (dist[nei], nei))

    print(*dist)


if __name__ == "__main__":

    n, m = map(int, input().split())

    graph = {}

    for _ in range(m):
        a, b, c = map(int, input().split())

        a -= 1
        b -= 1

        if a not in graph:
            graph[a] = []

        graph[a].append((b, c))

    dijkstra(graph, n)