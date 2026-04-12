from typing import List
from collections import defaultdict

class Solution:

    def dfs(self, node, parent, graph, labels, result):
        freq = [0] * 26   # count of a-z

        # add current node label
        idx = ord(labels[node]) - ord('a')
        freq[idx] = 1

        for nei in graph[node]:
            if nei == parent:
                continue

            child_freq = self.dfs(nei, parent=node, graph=graph, labels=labels, result=result)

            # merge child frequencies
            for i in range(26):
                freq[i] += child_freq[i]

        # store result for this node
        result[node] = freq[idx]

        return freq

    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        result = [0] * n

        self.dfs(0, -1, graph, labels, result)

        return result