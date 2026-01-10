class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        rows = cols = len(isConnected)
        # solution
        provinces = 0
        visited = [False]*rows
        for i in range(rows):
            if not visited[i]:
                provinces+=1

                self.dfs(i, isConnected, visited)

        return provinces

    def dfs(self, node, isConnected, visited):
        visited[node] = True

        for neighbor in range(len(isConnected)):
            if isConnected[node][neighbor] == 1  and not visited[neighbor]:
                visited[neighbor] = True
                self.dfs(neighbor, isConnected, visited)
        
