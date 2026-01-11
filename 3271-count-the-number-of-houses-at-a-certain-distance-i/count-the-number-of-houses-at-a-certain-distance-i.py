from collections import deque, defaultdict

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        
        gr = [[float('inf') for j in range(n + 1)] for i in range(n + 1)]

        for i in range(2, n+1):
            j = i-1
            gr[j][j] = 0
            gr[i][i] = 0

            gr[i][j] = 1
            gr[j][i] = 1

        if x != y:
            gr[x][y] = 1
            gr[y][x] = 1

        # Floyd-Warshall algorithm
        for k in range(1, n+1):
            for i in range(1, n+1):
                for j in range(1, n+1):
                    gr[i][j] = min(gr[i][j], gr[i][k] + gr[k][j])

        # Use defaultdict to auto-initialize missing keys to 0
        freq = defaultdict(int)
        
        for i in range(1, n+1):
            for j in range(1, n+1):
                freq[gr[i][j]] += 1

        result = [0] * n

        for i in range(1, n+1):
            if i in freq:
                result[i-1] = freq[i]

        return result