from collections import deque

def multiSourceBFS(graph, sources):
    q = deque()
    dist = {}
    visited = set()

    # Push all source nodes
    for s in sources:
        q.append(s)
        visited.add(s)
        dist[s] = 0

    while q:
        node = q.popleft()

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                dist[nei] = dist[node] + 1
                q.append(nei)

    return dist


# Example graph
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2, 4],
    4: [3]
}

sources = [0, 4]

print(multiSourceBFS(graph, sources))
