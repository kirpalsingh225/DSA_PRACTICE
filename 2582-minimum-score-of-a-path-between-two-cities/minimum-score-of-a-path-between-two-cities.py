class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = {}
        
        # Build adjacency list
        for start, end, d in roads:
            if start not in graph:
                graph[start] = []
            if end not in graph:
                graph[end] = []
            
            graph[start].append((end, d))
            graph[end].append((start, d))
        
        result = float("inf")
        visited = set()
        
        def dfs(node):
            nonlocal result
            visited.add(node)
            
            # Check all edges connected to this node
            for neighbor, distance in graph.get(node, []):
                result = min(result, distance)
                
                if neighbor not in visited:
                    dfs(neighbor)
        
        # Start DFS from node 1
        dfs(1)
        
        return result