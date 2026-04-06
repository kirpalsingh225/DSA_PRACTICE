class Solution:

    def dfs(self, stones, index, visited):
        visited.add(index)

        for i in range(len(stones)):
            r = stones[index][0]
            c = stones[index][1]
            if i not in visited and (stones[i][0]==r or stones[i][1]==c):
                self.dfs(stones, i, visited)


    def removeStones(self, stones: List[List[int]]) -> int:
        
        n = len(stones)
        visited = set()

        group = 0
        for i in range(n):
            if i in visited:
                continue

            self.dfs(stones, i, visited)
            group+=1


        return n-group