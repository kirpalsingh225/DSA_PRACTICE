class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        degree = [0]*n

        for edge in edges:
            u = edge[0]
            v = edge[1]

            degree[v]+=1

        
        count = 0
        index = -1
        for i in range(n):
            if degree[i] == 0:
                count+=1
                index = i

        if count == 1:
            return index

        return -1