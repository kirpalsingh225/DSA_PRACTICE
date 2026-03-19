def score(edges, n):
    # Step 1: convert weights
    new_edges = []
    for u, v, w in edges:
        new_edges.append((u, v, -w))

    dist = [float('inf')] * (n + 1)
    dist[1] = 0

    # Step 2: Bellman-Ford
    for _ in range(n - 1):
        for u, v, w in new_edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Step 3: detect negative cycle affecting node n
    affected = [False] * (n + 1)

    for _ in range(n):
        for u, v, w in new_edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                affected[v] = True
            if affected[u]:
                affected[v] = True

    # Step 4: check if n is affected
    if affected[n]:
        print(-1)  # infinite score
    else:
        print(-dist[n])  # convert back


if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = []

    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))

    score(edges, n)
