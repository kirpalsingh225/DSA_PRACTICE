from collections import deque


def helper(graph, n):
    q = deque()

    q.append([0, 0])

    distance = [float('inf')]*n

    distance[0] = 0

    while q:
        curr_node, dist = q.popleft()


        for neighbor in graph.get(curr_node, []):
            neigh_node = neighbor[0]
            neigh_dist = neighbor[1]

            if dist + neigh_dist < distance[neigh_node]:
                distance[neigh_node] = dist + neigh_dist 
                q.append([neigh_node, distance[neigh_node]])



    ways = [0]*n
    ways[0] = 1

    q = deque()
    q.append([0, 0])

    while q:
        curr_node, dist = q.popleft()


        for neighbor in graph.get(curr_node, []):
            neigh_node = neighbor[0]
            neigh_dist = neighbor[1]

            if dist + neigh_dist == distance[neigh_node]:
                ways[neigh_node] = (ways[neigh_node] + ways[curr_node]) % (10**9+7)
                q.append(neigh_node)

