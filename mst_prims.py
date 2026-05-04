import heapq

def prims(n, edges):
    # Build adjacency list
    graph = {i: [] for i in range(n)}
    for u, v, w in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))  # undirected graph

    visited = set()
    min_heap = [(0, 0)]  # (weight, node)
    total_cost = 0

    while min_heap and len(visited) < n:
        weight, node = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)
        total_cost += weight

        for neigh_weight, neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (neigh_weight, neighbor))

    return total_cost


if __name__ == "__main__":
    # number of nodes
    n = 5

    # edges: (u, v, weight)
    edges = [
        (0, 1, 2),
        (0, 3, 6),
        (1, 2, 3),
        (1, 3, 8),
        (1, 4, 5),
        (2, 4, 7),
        (3, 4, 9)
    ]

    result = prims(n, edges)
    print("Minimum Spanning Tree Cost:", result)
