class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = {}
        directed_graph = {}

        for a, b in connections:

            if a not in graph:
                graph[a] = []

            graph[a].append(b)

            if a not in directed_graph:
                directed_graph[a] = []
            directed_graph[a].append(b)


            if b not in graph:
                graph[b] = []
            graph[b].append(a)

        visited = set()
        edges = 0
        def dfs(graph, root, prev_node):
            nonlocal edges
            visited.add(root)

            if prev_node != -1 and prev_node not in directed_graph.get(root, []):
                edges+=1

            for neighbor in graph[root]:
                if neighbor not in visited:
                    dfs(graph, neighbor, root)

        dfs(graph, 0, -1)
        return edges