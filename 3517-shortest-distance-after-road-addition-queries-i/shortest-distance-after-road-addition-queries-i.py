from collections import deque
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for i in range(n-1):
            u = i
            v = i+1

            graph[u].append(v)

        result = [0]*(len(queries))

        for i in range(len(queries)):
            u = queries[i][0]
            v = queries[i][1]

            graph[u].append(v)

            q = deque()
            q.append([0, 0])
            visited = set()
            visited.add(0)

            while q:
                curr, dist = q.popleft()

                if curr == n-1:
                    result[i] = dist
                    break

                for neighbor in graph.get(curr):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append([neighbor, dist+1])


        return result