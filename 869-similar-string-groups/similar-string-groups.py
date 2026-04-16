class Solution:
    def isSimiliar(self, str1, str2):
        m = len(str1)
        diff = 0

        for i in range(m):
            if str1[i] != str2[i]:
                diff+=1

        return diff == 2 or diff == 0

    def dfs(self, graph, visited, src):
        visited.add(src)

        for n in graph.get(src, []):
            if n not in visited:
                self.dfs(graph, visited, n)

    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)

        graph = defaultdict(list)

        for i in range(n):
            for j in range(i+1, n):
                if self.isSimiliar(strs[i], strs[j]):
                    graph[i].append(j)
                    graph[j].append(i)


        visited = set()
        count = 0

        for i in range(n):
            if i not in visited:
                self.dfs(graph, visited, i)
                count+=1


        return count
