class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        
        degree = [0]*n

        for road in roads:
            u = road[0]
            v = road[1]

            degree[u]+=1
            degree[v]+=1

        degree = sorted(degree)

        value = 1
        ans = 0

        for i in range(n):
            ans+=degree[i]*(i+1)
            value+=1

        return ans
