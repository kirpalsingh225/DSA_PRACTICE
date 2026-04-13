from typing import List
from collections import defaultdict

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        graph = defaultdict(list)

        # build tree
        for i in range(1, n):
            graph[parent[i]].append(i)

        self.result = 1  # at least 1 node

        def dfs(node):
            longest = 0
            second_longest = 0

            for child in graph[node]:
                child_len = dfs(child)

                # skip if same character
                if s[child] == s[node]:
                    continue

                # maintain top 2 lengths
                if child_len > longest:
                    second_longest = longest
                    longest = child_len
                elif child_len > second_longest:
                    second_longest = child_len

            # update global result
            self.result = max(self.result, 1 + longest + second_longest)

            # return longest path including this node
            return 1 + longest

        dfs(0)
        return self.result