def negative_cycle(edges, n):

    dist = [float('inf')] * (n + 1)
    dist[1] = 0

    # Relax edges n-1 times
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Check one more time
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            print("negative cycle found")
            return

    print("no negative cycle found")
