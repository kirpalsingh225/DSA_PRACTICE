class Solution:


    def dfs(self, graph, current, parent, hasApple):
        time = 0

        for child in graph[current]:
            if child==parent:
                continue

            time_from_my_child = self.dfs(graph, child, current, hasApple)

            if time_from_my_child > 0 or hasApple[child]==True:
                time+=time_from_my_child+2

        return time

    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)

        for edge in edges:
            u = edge[0]
            v = edge[1]

            graph[u].append(v)
            graph[v].append(u)

        return self.dfs(graph, 0, -1, hasApple)