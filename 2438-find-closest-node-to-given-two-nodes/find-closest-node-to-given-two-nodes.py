from collections import deque
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        graph = defaultdict(list)

        for i in range(len(edges)):
            u = i 
            v = edges[i]

            if v == -1:
                continue

            graph[u].append(v)


        dist1 = [float('inf')]*n
        dist2 = [float('inf')]*n

        q = deque()
        visited = set()

        q.append([node1, 0])
        visited.add(node1)

        while q:
            curr, dist = q.popleft()

            dist1[curr] = dist

            for neighbor in graph.get(curr, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append([neighbor, dist+1])


        q = deque()
        visited = set()

        q.append([node2, 0])
        visited.add(node2)

        while q:
            curr, dist = q.popleft()

            dist2[curr] = dist

            for neighbor in graph.get(curr, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append([neighbor, dist+1])


        min_dist = float('inf')
        answer = -1

        for i in range(n):
            if dist1[i] == float("inf") or dist2[i] == float("inf"):
                continue

            curr_max = max(dist1[i], dist2[i])

            if curr_max < min_dist:
                min_dist = curr_max
                answer = i


        return answer


            



