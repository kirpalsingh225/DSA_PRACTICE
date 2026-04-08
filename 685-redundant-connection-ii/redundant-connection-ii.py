
class DSU:
        def __init__(self, n):
            self.parent = list(range(n))

        def find(self, x):
            if x != self.parent[x]:
                self.parent[x] = self.find(self.parent[x])  # path compression
            return self.parent[x]

        def union(self, x, y):
            px = self.find(x)
            py = self.find(y)

            if px == py:
                return False   # already connected

            self.parent[py] = px
            return True
class Solution:

    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        edge1, edge2 = None, None
        point_to = {}

        for u, v in edges:
            if v in point_to:
                edge2 = [u, v]
                edge1 = [point_to[v], v]

            point_to[v] = u

        uf = DSU(len(edges)+1)

        for edge in edges:
            if edge!=edge2:
                if not uf.union(edge[0], edge[1]):
                    if edge1:
                        return edge1
                    else:
                        return edge


        return edge2
