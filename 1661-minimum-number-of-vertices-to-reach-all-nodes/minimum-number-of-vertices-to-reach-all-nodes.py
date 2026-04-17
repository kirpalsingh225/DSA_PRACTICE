class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        indegree = [False]*n

        for edge in edges:
            u = edge[0]
            v = edge[1]

            indegree[v] = True


        result = []

        for i in range(n):
            if indegree[i] == 0:
                result.append(i)


        return result