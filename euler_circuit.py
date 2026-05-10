from collections import defaultdict

def hasEulerCircuit(edges):
    graph = defaultdict(list)
    degree = defaultdict(int)

    # Build graph and count degree
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

        degree[u] += 1
        degree[v] += 1

    # Check all degrees are even
    for node in degree:
        if degree[node] % 2 != 0:
            return False

    return True


# Example
edges = [
    [0, 1],
    [1, 2],
    [2, 0]
]

print(hasEulerCircuit(edges))  # True
