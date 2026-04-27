from collections import deque, defaultdict
from typing import List

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        
        n = len(colors)
        graph = defaultdict(list)
        indegree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        q = deque()
        t = [[0] * 26 for _ in range(n)]

        # initialize
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
                t[i][ord(colors[i]) - ord('a')] = 1

        answer = 0
        countNodes = 0

        while q:
            curr = q.popleft()
            countNodes += 1

            answer = max(answer, t[curr][ord(colors[curr]) - ord('a')])

            for v in graph[curr]:
                for i in range(26):
                    add = 1 if i == ord(colors[v]) - ord('a') else 0
                    t[v][i] = max(t[v][i], t[curr][i] + add)

                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        # cycle check
        if countNodes < n:
            return -1

        return answer