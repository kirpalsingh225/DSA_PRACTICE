def findCircleNum(isConnected):
    n = len(isConnected)
    visited = [False] * n

    def dfs(city):
        visited[city] = True

        for neighbor in range(n):
            if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)

    provinces = 0

    for city in range(n):
        if not visited[city]:
            dfs(city)
            provinces += 1

    return provinces


# Example
isConnected = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]

print(findCircleNum(isConnected))
