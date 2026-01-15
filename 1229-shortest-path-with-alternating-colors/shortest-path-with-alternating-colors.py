class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = {}
        answer = [-1]*n

        for i in redEdges:
            a = i[0]
            b = i[1]
            if a not in graph:
                graph[a] = []

            
            graph[a].append((b, "red"))

        for i in blueEdges:
            a = i[0]
            b = i[1]
            if a not in graph:
                graph[a] = []

            
            graph[a].append((b, "blue"))

        
        visited = set()
        q = deque()

        visited.add((0, "red"))
        visited.add((0, "blue"))
        q.append([0, 0, "red"])
        q.append([0, 0, "blue"])
        answer[0] = 0

        idx = 0
        while q:
            curr, dist, prev_color = q.popleft()

            if answer[curr] == -1 or answer[curr] > dist:  # Changed this line
                answer[curr] = dist

            

            for neighbor in graph.get(curr, []):
                n = neighbor[0]
                color = neighbor[1]

                if (n, color) not in visited and prev_color!=color:
                    visited.add((n, color))
                    q.append([n, dist+1, color])

        return answer