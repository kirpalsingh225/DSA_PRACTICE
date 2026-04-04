from typing import List
from collections import defaultdict

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        p = list(range(n))

        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                p[py] = px

        # Step 1: Build DSU
        for x, y in pairs:
            union(x, y)

        # Step 2: Group indices by root
        groups = defaultdict(list)
        for i in range(n):
            root = find(i)
            groups[root].append(i)

        # Step 3: Build result
        res = list(s)
        for indices in groups.values():
            chars = sorted(res[i] for i in indices)
            indices.sort()

            for i, c in zip(indices, chars):
                res[i] = c

        return "".join(res)