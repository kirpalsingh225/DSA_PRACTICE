from collections import deque
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = {}

        for i in edges:
            a = i[0]
            b = i[1]

            if b not in graph:
                graph[b] = []

            graph[b].append(a)

        
        answer = []
        for i in range(0, n):
                visited = set()
                q = deque()
                visited.add(i)
                q.append(i)
                result = []
                while q:
                    curr = q.popleft()

                    for neighbor in graph.get(curr, []):
                        if neighbor not in visited:
                            result.append(neighbor)
                            visited.add(neighbor)
                            q.append(neighbor)


                answer.append(sorted(result))


        return answer
