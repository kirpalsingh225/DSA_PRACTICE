from typing import List

class Solution:

    def find(self, x, parent):
        if parent[x] != x:
            parent[x] = self.find(parent[x], parent)  # path compression
        return parent[x]

    def union(self, x, y, parent):
        px = self.find(x, parent)
        py = self.find(y, parent)

        if px != py:
            parent[py] = px   # attach root

    def equationsPossible(self, equations: List[str]) -> bool:
        parent = list(range(26))  # a-z

        # Step 1: process ==
        for s in equations:
            if s[1] == '=':
                x = ord(s[0]) - ord('a')
                y = ord(s[3]) - ord('a')
                self.union(x, y, parent)

        # Step 2: process !=
        for s in equations:
            if s[1] == '!':
                x = ord(s[0]) - ord('a')
                y = ord(s[3]) - ord('a')

                if self.find(x, parent) == self.find(y, parent):
                    return False

        return True