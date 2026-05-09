from collections import defaultdict, deque

def bfs_farthest(start, graph):
    visited = set([start])
    q = deque([(start, 0)])

    farthest_node = start
    max_dist = 0

    while q:
        node, dist = q.popleft()

        if dist > max_dist:
            max_dist = dist
            farthest_node = node

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append((nei, dist + 1))

    return farthest_node, max_dist


def tree_diameter(edges):
    graph = defaultdict(list)

    # Build graph
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    start = edges[0][0]

    far_node, _ = bfs_farthest(start, graph)

    other_end, diameter = bfs_farthest(far_node, graph)

    return diameter


# Example
edges = [
    [0, 1],
    [1, 2],
    [2, 3],
    [1, 4],
    [4, 5]
]

print(tree_diameter(edges)) 
