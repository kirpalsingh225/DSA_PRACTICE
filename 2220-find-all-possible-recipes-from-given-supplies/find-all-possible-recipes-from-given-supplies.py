from collections import deque
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        n = len(recipes)
        indegree = [0]*n
        graph = {}
        visited = set(supplies)

        for i in range(len(recipes)):
            for j in ingredients[i]:
                if j not in visited:
                    if j not in graph:  
                        graph[j] = []
                    graph[j].append(i)
                    indegree[i]+=1

        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        result = []  
        while q:
            curr = q.popleft()
            recipe = recipes[curr]
            result.append(recipe)

            if recipe in graph:  # Check if recipe exists in graph
                for neighbor in graph[recipe]:  
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        q.append(neighbor)

        return result