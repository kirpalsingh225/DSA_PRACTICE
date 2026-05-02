class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False

        # Union by rank
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1

        return True


def kruskal(n, edges):
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])

    ds = DisjointSet(n)
    mst = []
    total_cost = 0

    for u, v, w in edges:
        if ds.union(u, v):
            mst.append((u, v, w))
            total_cost += w

    return mst, total_cost
